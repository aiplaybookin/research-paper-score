"""Data models for the research paper scoring library."""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class ChunkScore:
    """Represents a score for a single text chunk/section."""
    section_name: str
    text: str
    score: float
    reasoning: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class ScoringResult:
    """Represents the complete scoring result for a research paper."""
    paper_path: str
    chunk_scores: List[ChunkScore]
    average_score: float
    total_chunks: int
    processing_time: float
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_chunks(cls, paper_path: str, chunk_scores: List[ChunkScore], 
                   processing_time: float, metadata: Optional[Dict[str, Any]] = None) -> 'ScoringResult':
        """Create a ScoringResult from a list of chunk scores."""
        if not chunk_scores:
            average_score = 0.0
        else:
            average_score = sum(chunk.score for chunk in chunk_scores) / len(chunk_scores)
        
        return cls(
            paper_path=paper_path,
            chunk_scores=chunk_scores,
            average_score=average_score,
            total_chunks=len(chunk_scores),
            processing_time=processing_time,
            metadata=metadata or {}
        )


@dataclass
class TextChunk:
    """Represents a chunk of text extracted from a research paper."""
    section_name: str
    text: str
    page_number: Optional[int] = None
    position: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None