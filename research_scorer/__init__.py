"""Research Paper Scoring Library

A Python library for extracting text from research papers and scoring them using Claude Haiku 3.5.
"""

from .paper_scorer import PaperScorer
from .pdf_processor import PDFProcessor
from .text_chunker import TextChunker
from .claude_scorer import ClaudeScorer
from .models import ScoringResult, ChunkScore

__version__ = "0.1.0"
__all__ = ["PaperScorer", "PDFProcessor", "TextChunker", "ClaudeScorer", "ScoringResult", "ChunkScore"]