"""Demo script to test contextual scoring with memory."""

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
    
    print("🧠 Testing Contextual Scoring with Memory")
    print("=" * 50)
    
    # Test with contextual memory enabled
    print("\n🔍 Testing WITH contextual memory...")
    scorer_with_context = PaperScorer(
        api_key=api_key,
        use_context=True,
        save_detailed_results=True,
        results_dir="results_with_context"
    )
    
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found")
        return
    
    test_paper = pdf_files[1]
    print(f"📄 Processing: {test_paper.name}")
    
    try:
        result_with_context = scorer_with_context.score_paper(str(test_paper))
        
        print(f"\n✅ Contextual Analysis Complete!")
        print(f"   Overall Score: {result_with_context.average_score:.2f}/10")
        print(f"   Sections: {result_with_context.total_chunks}")
        
        print(f"\n📊 Section Scores (WITH context):")
        for chunk_score in result_with_context.chunk_scores:
            summary = chunk_score.metadata.get("summary", "")
            summary_preview = summary[:60] + "..." if len(summary) > 60 else summary
            print(f"   {chunk_score.section_name}: {chunk_score.score:.1f}/10")
            if summary:
                print(f"     📝 Summary: {summary_preview}")
        
        # Show how context builds up
        print(f"\n🔗 Context Memory Building:")
        context_summaries = []
        for i, chunk_score in enumerate(result_with_context.chunk_scores):
            summary = chunk_score.metadata.get("summary", "")
            if summary:
                context_summaries.append(f"{chunk_score.section_name}: {summary}")
                print(f"   Step {i+1}: Added context for '{chunk_score.section_name}'")
                if i < 3:  # Show first few contexts
                    print(f"            → {summary[:50]}...")
        
        print(f"\n📁 Results saved with context summaries in markdown files")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()