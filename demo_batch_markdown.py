"""Demo script to test batch processing with markdown export."""

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
    
    print("🚀 Testing batch processing with markdown export...")
    
    # Get first 2 papers for demo (to avoid long processing time)
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))[:2]
    
    if len(pdf_files) < 2:
        print("Need at least 2 PDF files for batch demo")
        return
    
    print(f"📄 Processing {len(pdf_files)} papers:")
    for pdf in pdf_files:
        print(f"   - {pdf.name}")
    
    try:
        # This will create individual markdown files + batch summary
        results = scorer.batch_process_with_markdown([str(f) for f in pdf_files])
        
        print(f"\n✅ Batch processing complete!")
        print(f"   Papers processed: {len(results)}")
        
        # Show what files were created
        results_dir = Path("results")
        if results_dir.exists():
            md_files = list(results_dir.glob("*.md"))
            print(f"\n📁 Markdown files created: {len(md_files)}")
            
            # Separate individual analyses from batch summary
            individual_files = [f for f in md_files if "_analysis_" in f.name]
            batch_files = [f for f in md_files if "batch_summary_" in f.name]
            
            print(f"   Individual analyses: {len(individual_files)}")
            for md_file in individual_files:
                print(f"     - {md_file.name}")
            
            print(f"   Batch summaries: {len(batch_files)}")
            for md_file in batch_files:
                print(f"     - {md_file.name}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()