"""Quick demo of batch processing capability."""

import os
from pathlib import Path
from dotenv import load_dotenv
from research_scorer import PaperScorer

def main():
    load_dotenv()
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        return
    
    scorer = PaperScorer(api_key=api_key)
    
    # Get first 2 papers for quick demo
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))[:2]
    
    print(f"🚀 Batch processing {len(pdf_files)} papers...")
    
    results = scorer.score_multiple_papers([str(f) for f in pdf_files])
    summary = scorer.get_summary_report(results)
    
    print(f"\n📈 Batch Results:")
    print(f"   Papers Processed: {summary['total_papers']}")
    print(f"   Average Score: {summary['average_score']:.2f}")
    print(f"   Score Range: {summary['lowest_score']:.2f} - {summary['highest_score']:.2f}")
    
    print(f"\n📄 Individual Papers:")
    for paper in summary['papers']:
        paper_name = Path(paper['path']).name
        print(f"   {paper_name}: {paper['score']:.2f}/10 ({paper['chunks']} sections)")

if __name__ == "__main__":
    main()