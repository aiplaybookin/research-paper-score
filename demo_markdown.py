"""Demo script to test markdown export functionality."""

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
    
    # Initialize scorer with markdown saving enabled
    scorer = PaperScorer(
        api_key=api_key,
        save_detailed_results=True,
        results_dir="results"
    )
    
    print("🚀 Testing markdown export functionality...")
    
    # Test with one paper
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found")
        return
    
    test_paper = pdf_files[8]
    print(f"📄 Processing: {test_paper.name}")
    
    try:
        # This will automatically save a detailed markdown file
        result = scorer.score_paper(str(test_paper))
        
        print(f"✅ Analysis complete!")
        print(f"   Score: {result.average_score:.2f}/10")
        print(f"   Sections: {result.total_chunks}")
        
        # Check if results directory was created
        results_dir = Path("results")
        if results_dir.exists():
            md_files = list(results_dir.glob("*.md"))
            print(f"📁 Markdown files created: {len(md_files)}")
            for md_file in md_files:
                print(f"   - {md_file.name}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()