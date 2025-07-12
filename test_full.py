"""Test the complete scoring pipeline with Claude API."""

import os
from pathlib import Path
from dotenv import load_dotenv
from research_scorer import PaperScorer

def main():
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment")
        return
    
    print("✓ API key loaded successfully")
    
    # Initialize scorer
    scorer = PaperScorer(api_key=api_key)
    print("✓ PaperScorer initialized")
    
    # Find a test paper
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in papers directory")
        return
    
    # Test with the first paper
    test_paper = pdf_files[0]
    print(f"\n🔍 Testing with: {test_paper.name}")
    
    try:
        # Score the paper
        result = scorer.score_paper(str(test_paper))
        
        print(f"\n📊 Results:")
        print(f"   Average Score: {result.average_score:.2f}/10")
        print(f"   Sections Analyzed: {result.total_chunks}")
        print(f"   Processing Time: {result.processing_time:.1f}s")
        
        print(f"\n📝 Section Breakdown:")
        for chunk_score in result.chunk_scores:
            print(f"   {chunk_score.section_name}: {chunk_score.score:.1f}/10")
            if chunk_score.reasoning:
                reasoning_preview = chunk_score.reasoning[:80] + "..." if len(chunk_score.reasoning) > 80 else chunk_score.reasoning
                print(f"      → {reasoning_preview}")
        
        print(f"\n✅ Successfully scored {test_paper.name}")
        
    except Exception as e:
        print(f"❌ Error scoring paper: {e}")

if __name__ == "__main__":
    main()