"""Main paper scoring orchestrator."""

import time
from datetime import datetime
from typing import List, Optional, Dict, Any
from pathlib import Path

from .models import ScoringResult, TextChunk
from .pdf_processor import PDFProcessor
from .text_chunker import TextChunker
from .claude_scorer import ClaudeScorer


class PaperScorer:
    """Main class for scoring research papers."""
    
    def __init__(self, 
                 api_key: str,
                 model: str = "claude-3-5-haiku-20241022",
                 max_chunk_size: int = 4000,
                 min_chunk_size: int = 100,
                 delay_between_requests: float = 1.0,
                 save_detailed_results: bool = True,
                 results_dir: str = "results",
                 use_context: bool = True):
        """Initialize the paper scorer.
        
        Args:
            api_key: Anthropic API key
            model: Claude model to use
            max_chunk_size: Maximum size for text chunks
            min_chunk_size: Minimum size for text chunks
            delay_between_requests: Delay between API calls in seconds
            save_detailed_results: Whether to save detailed results as markdown
            results_dir: Directory to save detailed results
            use_context: Whether to use contextual memory from previous sections
        """
        self.pdf_processor = PDFProcessor()
        self.text_chunker = TextChunker(max_chunk_size, min_chunk_size)
        self.claude_scorer = ClaudeScorer(api_key, model, use_context)
        self.delay_between_requests = delay_between_requests
        self.save_detailed_results = save_detailed_results
        self.results_dir = Path(results_dir)
        
        # Create results directory if it doesn't exist
        if self.save_detailed_results:
            self.results_dir.mkdir(exist_ok=True)
        
    def score_paper(self, 
                   pdf_path: str,
                   system_prompt: Optional[str] = None,
                   custom_config: Optional[Dict[str, Any]] = None) -> ScoringResult:
        """Score a research paper and return comprehensive results.
        
        Args:
            pdf_path: Path to the PDF file
            system_prompt: Custom system prompt for scoring
            custom_config: Additional configuration options
            
        Returns:
            ScoringResult object with scores and metadata
        """
        start_time = time.time()
        
        try:
            # Reset context for new paper
            self.claude_scorer.reset_context()
            
            # Step 1: Extract text and create initial chunks
            print(f"Processing PDF: {pdf_path}")
            chunks = self.pdf_processor.process_pdf(pdf_path)
            print(f"Extracted {len(chunks)} initial sections")
            
            # Step 2: Process chunks (split large ones, filter small ones)
            chunks = self.text_chunker.split_large_chunks(chunks)
            chunks = self.text_chunker.filter_chunks(chunks)
            print(f"Final chunk count: {len(chunks)}")
            
            if not chunks:
                raise ValueError("No valid text chunks found in the PDF")
            
            # Step 3: Score each chunk
            print("Scoring chunks with Claude...")
            chunk_scores = self.claude_scorer.score_chunks(
                chunks, 
                system_prompt, 
                self.delay_between_requests
            )
            
            # Step 4: Create result
            processing_time = time.time() - start_time
            
            metadata = {
                "pdf_path": pdf_path,
                "model_used": self.claude_scorer.model,
                "processing_config": {
                    "max_chunk_size": self.text_chunker.max_chunk_size,
                    "min_chunk_size": self.text_chunker.min_chunk_size,
                    "delay_between_requests": self.delay_between_requests
                }
            }
            
            if custom_config:
                metadata.update(custom_config)
            
            result = ScoringResult.from_chunks(
                paper_path=pdf_path,
                chunk_scores=chunk_scores,
                processing_time=processing_time,
                metadata=metadata
            )
            
            print(f"Scoring completed in {processing_time:.2f} seconds")
            print(f"Average score: {result.average_score:.2f}")
            
            # Save detailed results if enabled
            if self.save_detailed_results:
                self.save_detailed_markdown(result)
            
            return result
            
        except Exception as e:
            processing_time = time.time() - start_time
            raise Exception(f"Error scoring paper: {str(e)}")
    
    def score_multiple_papers(self, 
                            pdf_paths: List[str],
                            system_prompt: Optional[str] = None) -> List[ScoringResult]:
        """Score multiple research papers."""
        results = []
        
        for pdf_path in pdf_paths:
            try:
                result = self.score_paper(pdf_path, system_prompt)
                results.append(result)
            except Exception as e:
                print(f"Error processing {pdf_path}: {str(e)}")
                continue
        
        return results
    
    def get_summary_report(self, results: List[ScoringResult]) -> Dict[str, Any]:
        """Generate a summary report for multiple papers."""
        if not results:
            return {"error": "No results to summarize"}
        
        scores = [r.average_score for r in results]
        
        return {
            "total_papers": len(results),
            "average_score": sum(scores) / len(scores),
            "highest_score": max(scores),
            "lowest_score": min(scores),
            "papers": [
                {
                    "path": r.paper_path,
                    "score": r.average_score,
                    "chunks": r.total_chunks
                }
                for r in results
            ]
        }
    
    def save_detailed_markdown(self, result: ScoringResult) -> str:
        """Save detailed scoring results as a markdown file.
        
        Args:
            result: ScoringResult to save
            
        Returns:
            Path to the saved markdown file
        """
        # Generate filename from paper path
        paper_name = Path(result.paper_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        md_filename = f"{paper_name}_analysis_{timestamp}.md"
        md_path = self.results_dir / md_filename
        
        # Generate markdown content
        md_content = self._generate_markdown_content(result)
        
        # Save to file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Detailed results saved to: {md_path}")
        return str(md_path)
    
    def _generate_markdown_content(self, result: ScoringResult) -> str:
        """Generate markdown content for the scoring result."""
        paper_name = Path(result.paper_path).name
        analysis_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Research Paper Analysis: {paper_name}

## Summary

| Metric | Value |
|--------|-------|
| **Paper** | {paper_name} |
| **Analysis Date** | {analysis_date} |
| **Overall Score** | **{result.average_score:.2f}/10** |
| **Sections Analyzed** | {result.total_chunks} |
| **Processing Time** | {result.processing_time:.2f} seconds |
| **Model Used** | {result.metadata.get('model_used', 'N/A')} |

## Score Distribution

"""
        
        # Add score distribution
        for chunk_score in result.chunk_scores:
            score_bar = "🟩" * int(chunk_score.score) + "⬜" * (10 - int(chunk_score.score))
            content += f"- **{chunk_score.section_name}**: {chunk_score.score:.1f}/10 {score_bar}\n"
        
        content += "\n---\n\n## Detailed Section Analysis\n\n"
        
        # Add detailed analysis for each section
        for i, chunk_score in enumerate(result.chunk_scores, 1):
            content += f"### {i}. {chunk_score.section_name}\n\n"
            content += f"**Score: {chunk_score.score:.1f}/10**\n\n"
            
            if chunk_score.reasoning:
                content += f"**Evaluation:**\n{chunk_score.reasoning}\n\n"
            
            # Add section summary if available
            summary = chunk_score.metadata.get("summary", "")
            if summary:
                content += f"**Summary:**\n{summary}\n\n"
            
            # Add text content in collapsible section
            content += f"<details>\n<summary>📄 View Section Content ({len(chunk_score.text)} characters)</summary>\n\n"
            content += f"```\n{chunk_score.text}\n```\n\n"
            content += "</details>\n\n"
            content += "---\n\n"
        
        # Add metadata section
        content += "## Technical Details\n\n"
        content += f"- **PDF Path**: `{result.paper_path}`\n"
        content += f"- **Processing Configuration**:\n"
        
        if 'processing_config' in result.metadata:
            config = result.metadata['processing_config']
            for key, value in config.items():
                content += f"  - {key}: {value}\n"
        
        content += f"\n*Analysis generated by Research Paper Scorer v0.1.0*\n"
        
        return content
    
    def batch_process_with_markdown(self, 
                                  pdf_paths: List[str],
                                  system_prompt: Optional[str] = None) -> List[ScoringResult]:
        """Score multiple papers and save markdown for each."""
        results = []
        
        for pdf_path in pdf_paths:
            try:
                result = self.score_paper(pdf_path, system_prompt)
                results.append(result)
            except Exception as e:
                print(f"Error processing {pdf_path}: {str(e)}")
                continue
        
        # Generate summary markdown
        if results:
            self._save_batch_summary_markdown(results)
        
        return results
    
    def _save_batch_summary_markdown(self, results: List[ScoringResult]) -> str:
        """Save a summary markdown for batch processing results."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_path = self.results_dir / f"batch_summary_{timestamp}.md"
        
        summary = self.get_summary_report(results)
        analysis_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Batch Analysis Summary

**Analysis Date**: {analysis_date}  
**Papers Processed**: {summary['total_papers']}  
**Average Score**: {summary['average_score']:.2f}/10  
**Score Range**: {summary['lowest_score']:.2f} - {summary['highest_score']:.2f}

## Results Overview

| Paper | Score | Sections | Status |
|-------|-------|----------|---------|
"""
        
        for paper in summary['papers']:
            paper_name = Path(paper['path']).name
            score_emoji = "🟢" if paper['score'] >= 7 else "🟡" if paper['score'] >= 5 else "🔴"
            content += f"| {paper_name} | {paper['score']:.2f}/10 | {paper['chunks']} | {score_emoji} |\n"
        
        content += f"\n## Score Distribution\n\n"
        
        scores = [r.average_score for r in results]
        score_ranges = [
            ("9-10 (Exceptional)", len([s for s in scores if s >= 9])),
            ("7-8 (Good)", len([s for s in scores if 7 <= s < 9])),
            ("5-6 (Average)", len([s for s in scores if 5 <= s < 7])),
            ("3-4 (Below Average)", len([s for s in scores if 3 <= s < 5])),
            ("1-2 (Poor)", len([s for s in scores if s < 3]))
        ]
        
        for range_name, count in score_ranges:
            if count > 0:
                content += f"- {range_name}: {count} papers\n"
        
        content += f"\n*Batch analysis generated by Research Paper Scorer v0.1.0*\n"
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Batch summary saved to: {summary_path}")
        return str(summary_path)