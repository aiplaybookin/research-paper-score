"""Basic test of the research scorer library."""

import os
from pathlib import Path
from research_scorer.pdf_processor import PDFProcessor
from research_scorer.text_chunker import TextChunker

def test_pdf_processing():
    """Test PDF processing without Claude API."""
    print("Testing PDF processing...")
    
    # Test with a sample PDF
    papers_dir = Path("papers")
    pdf_files = list(papers_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found for testing")
        return
    
    test_pdf = pdf_files[0]
    print(f"Testing with: {test_pdf}")
    
    # Test PDF processor
    processor = PDFProcessor()
    try:
        chunks = processor.process_pdf(str(test_pdf))
        print(f"✓ Extracted {len(chunks)} chunks")
        
        for i, chunk in enumerate(chunks[:3]):  # Show first 3 chunks
            print(f"  Chunk {i+1}: {chunk.section_name} ({len(chunk.text)} chars)")
        
    except Exception as e:
        print(f"✗ PDF processing failed: {e}")
        return
    
    # Test text chunker
    chunker = TextChunker()
    try:
        processed_chunks = chunker.split_large_chunks(chunks)
        filtered_chunks = chunker.filter_chunks(processed_chunks)
        print(f"✓ After processing: {len(filtered_chunks)} chunks")
        
    except Exception as e:
        print(f"✗ Text chunking failed: {e}")

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from research_scorer import PaperScorer, PDFProcessor, TextChunker, ClaudeScorer
        print("✓ All core classes imported successfully")
        
        from research_scorer.models import ScoringResult, ChunkScore, TextChunk
        print("✓ All model classes imported successfully")
        
    except Exception as e:
        print(f"✗ Import failed: {e}")

if __name__ == "__main__":
    test_imports()
    test_pdf_processing()