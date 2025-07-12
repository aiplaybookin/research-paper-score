"""PDF text extraction and processing for research papers."""

import re
import fitz  # PyMuPDF
from typing import List, Dict, Optional, Tuple
from pathlib import Path

from .models import TextChunk


class PDFProcessor:
    """Handles PDF text extraction with section detection for research papers."""
    
    def __init__(self):
        """Initialize the PDF processor."""
        self.section_patterns = [
            r'^(?:I\.?\s+)?(?:1\.?\s+)?INTRODUCTION',
            r'^(?:II\.?\s+)?(?:2\.?\s+)?(?:RELATED\s+WORK|BACKGROUND|LITERATURE\s+REVIEW)',
            r'^(?:III\.?\s+)?(?:3\.?\s+)?(?:METHODOLOGY|METHODS|APPROACH)',
            r'^(?:IV\.?\s+)?(?:4\.?\s+)?(?:EXPERIMENTS?|RESULTS?|EVALUATION)',
            r'^(?:V\.?\s+)?(?:5\.?\s+)?(?:DISCUSSION|ANALYSIS)',
            r'^(?:VI\.?\s+)?(?:6\.?\s+)?(?:CONCLUSION|CONCLUSIONS)',
            r'^(?:VII\.?\s+)?(?:7\.?\s+)?(?:FUTURE\s+WORK|LIMITATIONS)',
            r'^ABSTRACT',
            r'^REFERENCES?',
            r'^ACKNOWLEDGMENTS?',
            r'^APPENDIX'
        ]
        
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract raw text from PDF file."""
        try:
            doc = fitz.open(pdf_path)
            text = ""
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text += page.get_text()
                
            doc.close()
            return text
            
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    def detect_sections(self, text: str) -> List[Tuple[str, int, int]]:
        """Detect section boundaries in the text."""
        sections = []
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_clean = line.strip().upper()
            
            for pattern in self.section_patterns:
                if re.match(pattern, line_clean, re.IGNORECASE):
                    section_name = self._normalize_section_name(line_clean)
                    start_pos = sum(len(l) + 1 for l in lines[:i])
                    sections.append((section_name, start_pos, i))
                    break
        
        # Add end positions
        sections_with_ends = []
        for i, (name, start_pos, line_num) in enumerate(sections):
            if i < len(sections) - 1:
                end_pos = sections[i + 1][1]
            else:
                end_pos = len(text)
            sections_with_ends.append((name, start_pos, end_pos))
            
        return sections_with_ends
    
    def _normalize_section_name(self, section_line: str) -> str:
        """Normalize section names for consistency."""
        section_line = re.sub(r'^[IVX]+\.?\s*', '', section_line)
        section_line = re.sub(r'^\d+\.?\s*', '', section_line)
        
        normalized_names = {
            'INTRODUCTION': 'Introduction',
            'RELATED WORK': 'Related Work',
            'BACKGROUND': 'Background',
            'LITERATURE REVIEW': 'Literature Review',
            'METHODOLOGY': 'Methodology',
            'METHODS': 'Methods',
            'APPROACH': 'Approach',
            'EXPERIMENTS': 'Experiments',
            'EXPERIMENT': 'Experiments',
            'RESULTS': 'Results',
            'RESULT': 'Results',
            'EVALUATION': 'Evaluation',
            'DISCUSSION': 'Discussion',
            'ANALYSIS': 'Analysis',
            'CONCLUSION': 'Conclusion',
            'CONCLUSIONS': 'Conclusion',
            'FUTURE WORK': 'Future Work',
            'LIMITATIONS': 'Limitations',
            'ABSTRACT': 'Abstract',
            'REFERENCES': 'References',
            'REFERENCE': 'References',
            'ACKNOWLEDGMENTS': 'Acknowledgments',
            'ACKNOWLEDGMENT': 'Acknowledgments',
            'APPENDIX': 'Appendix'
        }
        
        return normalized_names.get(section_line.strip(), section_line.title())
    
    def chunk_by_sections(self, pdf_path: str) -> List[TextChunk]:
        """Extract text and chunk it by detected sections."""
        text = self.extract_text_from_pdf(pdf_path)
        sections = self.detect_sections(text)
        
        chunks = []
        
        if not sections:
            # If no sections detected, create a single chunk
            chunks.append(TextChunk(
                section_name="Full Document",
                text=text.strip(),
                metadata={"fallback": True}
            ))
        else:
            for section_name, start_pos, end_pos in sections:
                section_text = text[start_pos:end_pos].strip()
                
                if len(section_text) > 50:  # Skip very short sections
                    chunks.append(TextChunk(
                        section_name=section_name,
                        text=section_text,
                        metadata={"start_pos": start_pos, "end_pos": end_pos}
                    ))
        
        return chunks
    
    def process_pdf(self, pdf_path: str) -> List[TextChunk]:
        """Main method to process a PDF and return text chunks."""
        if not Path(pdf_path).exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
        return self.chunk_by_sections(pdf_path)