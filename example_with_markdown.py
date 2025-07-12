"""Example usage of the research paper scoring library with markdown export."""

import os
from pathlib import Path
from dotenv import load_dotenv
from research_scorer import PaperScorer

def main():
    load_dotenv()
    
    # Set up API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Please set ANTHROPIC_API_KEY environment variable")
        return
    
    print("🎯 Research Paper Scorer - Enhanced with Markdown Export")
    print("=" * 60)
    
    # Example 1: Score a single paper with markdown export
    print("\n📊 Example 1: Single Paper Analysis with Markdown Export")
    print("-" * 50)
    
    # Initialize scorer with markdown export enabled
    scorer = PaperScorer(
        api_key=api_key,
        save_detailed_results=True,  # Enable markdown export
        results_dir="results"        # Directory for markdown files
    )
    
    paper_path = "papers/Top1-2506.02064v1.pdf"
    
    if Path(paper_path).exists():
        try:
            print(f"Analyzing: {Path(paper_path).name}")
            result = scorer.score_paper(paper_path)
            
            print(f"✅ Analysis Complete!")
            print(f"   Overall Score: {result.average_score:.2f}/10")
            print(f"   Sections Analyzed: {result.total_chunks}")
            print(f"   Processing Time: {result.processing_time:.1f}s")
            
            print(f"\n📝 Section Breakdown:")
            for chunk_score in result.chunk_scores:
                score_emoji = "🟢" if chunk_score.score >= 7 else "🟡" if chunk_score.score >= 5 else "🔴"
                print(f"   {score_emoji} {chunk_score.section_name}: {chunk_score.score:.1f}/10")
                
        except Exception as e:
            print(f"❌ Error processing paper: {e}")
    else:
        print(f"Paper not found: {paper_path}")
    
    # Example 2: Batch processing with markdown export
    print(f"\n📚 Example 2: Batch Processing with Markdown Export")
    print("-" * 50)
    
    papers_dir = Path("papers")
    if papers_dir.exists():
        # Process first 2 papers for demo
        pdf_files = list(papers_dir.glob("*.pdf"))[:2]
        
        if pdf_files:
            try:
                print(f"Batch processing {len(pdf_files)} papers...")
                results = scorer.batch_process_with_markdown([str(f) for f in pdf_files])
                
                summary = scorer.get_summary_report(results)
                print(f"✅ Batch Processing Complete!")
                print(f"   Papers Processed: {summary['total_papers']}")
                print(f"   Average Score: {summary['average_score']:.2f}/10")
                print(f"   Score Range: {summary['lowest_score']:.2f} - {summary['highest_score']:.2f}")
                
                print(f"\n📊 Individual Results:")
                for paper in summary['papers']:
                    paper_name = Path(paper['path']).name
                    score_emoji = "🟢" if paper['score'] >= 7 else "🟡" if paper['score'] >= 5 else "🔴"
                    print(f"   {score_emoji} {paper_name}: {paper['score']:.2f}/10 ({paper['chunks']} sections)")
                    
            except Exception as e:
                print(f"❌ Error in batch processing: {e}")
        else:
            print("No PDF files found for batch processing")
    else:
        print("Papers directory not found")
    
    # Show created markdown files
    print(f"\n📁 Generated Files:")
    print("-" * 20)
    results_dir = Path("results")
    if results_dir.exists():
        md_files = sorted(results_dir.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
        if md_files:
            print(f"Markdown files created in {results_dir}/:")
            for md_file in md_files:
                size_kb = md_file.stat().st_size / 1024
                print(f"   📄 {md_file.name} ({size_kb:.1f} KB)")
        else:
            print("No markdown files found")
    else:
        print("Results directory not found")
    
    print(f"\n🎉 Demo Complete!")
    print(f"Check the 'results/' directory for detailed markdown analysis files.")

if __name__ == "__main__":
    main()