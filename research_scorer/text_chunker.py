"""Text chunking utilities for research papers."""

import re
from typing import List, Optional
from .models import TextChunk


class TextChunker:
    """Handles advanced text chunking strategies for research papers."""
    
    def __init__(self, max_chunk_size: int = 4000, min_chunk_size: int = 100):
        """Initialize the text chunker.
        
        Args:
            max_chunk_size: Maximum characters per chunk
            min_chunk_size: Minimum characters per chunk
        """
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
    
    def split_large_chunks(self, chunks: List[TextChunk]) -> List[TextChunk]:
        """Split chunks that are too large into smaller pieces."""
        processed_chunks = []
        
        for chunk in chunks:
            if len(chunk.text) <= self.max_chunk_size:
                processed_chunks.append(chunk)
            else:
                # Split large chunk into smaller pieces
                sub_chunks = self._split_text_intelligently(
                    chunk.text, 
                    chunk.section_name,
                    chunk.metadata
                )
                processed_chunks.extend(sub_chunks)
        
        return processed_chunks
    
    def _split_text_intelligently(self, text: str, section_name: str, 
                                metadata: Optional[dict] = None) -> List[TextChunk]:
        """Split text intelligently by paragraphs and sentences."""
        chunks = []
        
        # First try to split by paragraphs
        paragraphs = text.split('\n\n')
        
        current_chunk = ""
        chunk_num = 1
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
                
            # If adding this paragraph would exceed max size, save current chunk
            if current_chunk and len(current_chunk + para) > self.max_chunk_size:
                if len(current_chunk) >= self.min_chunk_size:
                    chunks.append(TextChunk(
                        section_name=f"{section_name} (Part {chunk_num})",
                        text=current_chunk.strip(),
                        metadata={**(metadata or {}), "chunk_part": chunk_num}
                    ))
                    chunk_num += 1
                current_chunk = para
            else:
                if current_chunk:
                    current_chunk += "\n\n" + para
                else:
                    current_chunk = para
        
        # Add the last chunk
        if current_chunk.strip() and len(current_chunk) >= self.min_chunk_size:
            chunks.append(TextChunk(
                section_name=f"{section_name} (Part {chunk_num})" if chunk_num > 1 else section_name,
                text=current_chunk.strip(),
                metadata={**(metadata or {}), "chunk_part": chunk_num}
            ))
        
        return chunks if chunks else [TextChunk(
            section_name=section_name,
            text=text,
            metadata=metadata
        )]
    
    def filter_chunks(self, chunks: List[TextChunk]) -> List[TextChunk]:
        """Filter out chunks that are too short or contain mostly references."""
        filtered_chunks = []
        
        for chunk in chunks:
            # Skip chunks that are too short
            if len(chunk.text) < self.min_chunk_size:
                continue
            
            # Skip chunks that are mostly references
            if self._is_mostly_references(chunk.text):
                continue
            
            # Skip chunks that are mostly figures/tables
            if self._is_mostly_figures_tables(chunk.text):
                continue
                
            filtered_chunks.append(chunk)
        
        return filtered_chunks
    
    def _is_mostly_references(self, text: str) -> bool:
        """Check if text is mostly bibliography/references."""
        lines = text.split('\n')
        reference_patterns = [
            r'^\[?\d+\]?\s*[A-Z].*\.\s*\d{4}',  # [1] Author, Title. Year
            r'^[A-Z][a-z]+,\s+[A-Z]\..*\(\d{4}\)',  # Author, A. Title (Year)
            r'^\d+\.\s+[A-Z].*\.\s*\d{4}',  # 1. Author, Title. Year
        ]
        
        reference_lines = 0
        for line in lines:
            line = line.strip()
            if any(re.match(pattern, line) for pattern in reference_patterns):
                reference_lines += 1
        
        # If more than 70% of lines look like references
        return reference_lines / len(lines) > 0.7 if lines else False
    
    def _is_mostly_figures_tables(self, text: str) -> bool:
        """Check if text is mostly figure/table captions."""
        # Count figure/table references
        fig_table_count = len(re.findall(r'(?:figure|table|fig\.|tab\.)\s*\d+', text, re.IGNORECASE))
        word_count = len(text.split())
        
        # If there are many figure/table references relative to content
        return fig_table_count > word_count / 50 if word_count > 0 else False