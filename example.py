"""Example usage of the research paper scoring library."""

import os
from pathlib import Path
from research_scorer import PaperScorer
from dotenv import load_dotenv
load_dotenv()

def main():
    # Set up API key (you'll need to set this)
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Please set ANTHROPIC_API_KEY environment variable")
        return
    
    # Initialize the scorer
    scorer = PaperScorer(api_key=api_key)
    
    # Example 1: Score a single paper
    print("=== Single Paper Example ===")
    paper_path = "papers/Top1-2506.02064v1.pdf"
    
    if Path(paper_path).exists():
        try:
            result = scorer.score_paper(paper_path)
            
            print(f"Paper: {result.paper_path}")
            print(f"Average Score: {result.average_score:.2f}")
            print(f"Total Chunks: {result.total_chunks}")
            print(f"Processing Time: {result.processing_time:.2f} seconds")
            
            print("\nSection Scores:")
            for chunk_score in result.chunk_scores:
                print(f"  {chunk_score.section_name}: {chunk_score.score:.1f}")
                if chunk_score.reasoning:
                    print(f"    Reasoning: {chunk_score.reasoning[:100]}...")
                print()
                
        except Exception as e:
            print(f"Error processing paper: {e}")
    else:
        print(f"Paper not found: {paper_path}")
    
    # Example 2: Score multiple papers
    print("\n=== Batch Processing Example ===")
    papers_dir = Path("papers")
    if papers_dir.exists():
        pdf_files = list(papers_dir.glob("*.pdf"))[:3]  # Process first 3 papers
        
        if pdf_files:
            try:
                results = scorer.score_multiple_papers([str(f) for f in pdf_files])
                summary = scorer.get_summary_report(results)
                
                print(f"Processed {summary['total_papers']} papers")
                print(f"Average Score: {summary['average_score']:.2f}")
                print(f"Score Range: {summary['lowest_score']:.2f} - {summary['highest_score']:.2f}")
                
                print("\nIndividual Results:")
                for paper in summary['papers']:
                    paper_name = Path(paper['path']).name
                    print(f"  {paper_name}: {paper['score']:.2f} ({paper['chunks']} chunks)")
                    
            except Exception as e:
                print(f"Error in batch processing: {e}")
        else:
            print("No PDF files found in papers directory")
    else:
        print("Papers directory not found")

if __name__ == "__main__":
    main()