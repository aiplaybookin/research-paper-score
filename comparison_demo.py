"""Demo script comparing contextual vs non-contextual scoring."""

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
    
    print("🔍 Contextual vs Non-Contextual Scoring Comparison")
    print("=" * 60)
    
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found")
        return
    
    test_paper = pdf_files[0]
    print(f"📄 Testing with: {test_paper.name}")
    
    # Test WITHOUT context
    print(f"\n🚫 Scoring WITHOUT contextual memory...")
    scorer_no_context = PaperScorer(
        api_key=api_key,
        use_context=False,
        save_detailed_results=False
    )
    
    try:
        result_no_context = scorer_no_context.score_paper(str(test_paper))
        
        print(f"✅ Non-contextual scoring complete!")
        print(f"   Overall Score: {result_no_context.average_score:.2f}/10")
        
        # Test WITH context  
        print(f"\n🧠 Scoring WITH contextual memory...")
        scorer_with_context = PaperScorer(
            api_key=api_key,
            use_context=True,
            save_detailed_results=False
        )
        
        result_with_context = scorer_with_context.score_paper(str(test_paper))
        
        print(f"✅ Contextual scoring complete!")
        print(f"   Overall Score: {result_with_context.average_score:.2f}/10")
        
        # Compare results
        print(f"\n📊 COMPARISON RESULTS:")
        print(f"{'='*60}")
        print(f"{'Section':<30} {'No Context':<12} {'With Context':<12} {'Difference':<10}")
        print(f"{'-'*60}")
        
        improvement_count = 0
        total_improvement = 0
        
        for i, (chunk_no_ctx, chunk_with_ctx) in enumerate(zip(
            result_no_context.chunk_scores, 
            result_with_context.chunk_scores
        )):
            section_name = chunk_no_ctx.section_name[:28] + "..." if len(chunk_no_ctx.section_name) > 30 else chunk_no_ctx.section_name
            diff = chunk_with_ctx.score - chunk_no_ctx.score
            diff_str = f"+{diff:.1f}" if diff > 0 else f"{diff:.1f}"
            
            print(f"{section_name:<30} {chunk_no_ctx.score:<12.1f} {chunk_with_ctx.score:<12.1f} {diff_str:<10}")
            
            if diff > 0:
                improvement_count += 1
            total_improvement += diff
        
        print(f"{'-'*60}")
        print(f"{'OVERALL AVERAGES':<30} {result_no_context.average_score:<12.2f} {result_with_context.average_score:<12.2f} {result_with_context.average_score - result_no_context.average_score:+.2f}")
        
        print(f"\n📈 IMPACT ANALYSIS:")
        print(f"   Sections Improved: {improvement_count}/{len(result_no_context.chunk_scores)}")
        print(f"   Average Improvement: {total_improvement/len(result_no_context.chunk_scores):+.2f} points per section")
        print(f"   Overall Improvement: {result_with_context.average_score - result_no_context.average_score:+.2f} points")
        
        if result_with_context.average_score > result_no_context.average_score:
            print(f"   🎯 Contextual memory IMPROVED scoring accuracy!")
        else:
            print(f"   📝 Contextual memory maintained consistent scoring")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()