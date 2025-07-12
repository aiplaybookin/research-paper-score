"""Claude API integration for scoring research paper sections."""

import asyncio
import time
from typing import List, Optional, Dict, Any
from anthropic import Anthropic

from .models import TextChunk, ChunkScore, DetailedScores


class ClaudeScorer:
    """Handles scoring of text chunks using Claude Haiku 3.5."""
    
    def __init__(self, api_key: str, model: str = "claude-3-5-haiku-20241022", use_context: bool = True):
        """Initialize the Claude scorer.
        
        Args:
            api_key: Anthropic API key
            model: Claude model to use for scoring
            use_context: Whether to use contextual memory from previous sections
        """
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.use_context = use_context
        self.default_system_prompt = self._get_default_system_prompt()
        self.context_memory = []  # Store summaries of previous sections
        
    def _get_default_system_prompt(self) -> str:
        """Get the default system prompt for research paper evaluation."""
        return """You are an expert research paper evaluator. Your task is to evaluate the quality of a section from a research paper and provide a score from 1-10.

IMPORTANT: When evaluating a section, consider that it is part of a complete research paper. Do NOT penalize a section for missing information that may have been covered in other sections of the paper. Focus on evaluating the quality and appropriateness of the content within the specific section's scope.

Consider these criteria when scoring:
1. **Clarity and Writing Quality** (1-2 points): Is the text well-written, clear, and easy to understand?
2. **Technical Depth** (1-2 points): Does the content demonstrate appropriate technical depth for the section?
3. **Novelty and Originality** (1-2 points): Does the content present novel ideas or approaches?
4. **Methodology Rigor** (1-2 points): Is the methodology sound and well-explained? (if applicable)
5. **Evidence and Support** (1-2 points): Are claims well-supported with evidence, citations, or experiments?

Scoring Guidelines:
- 9-10: Exceptional quality, publishable in top-tier venues
- 7-8: Good quality, suitable for publication with minor revisions
- 5-6: Average quality, needs significant improvements
- 3-4: Below average, major issues present
- 1-2: Poor quality, substantial problems

Provide your response in the following format:
Score: [numerical score 1-10]
Detailed Scores:
- Clarity and Writing Quality: [0-2]
- Technical Depth: [0-2]
- Novelty and Originality: [0-2]
- Methodology Rigor: [0-2]
- Evidence and Support: [0-2]
Reasoning: [brief explanation of your scoring rationale]
Summary: [2-3 sentence summary of the key points covered in this section]"""

    def score_chunk(self, chunk: TextChunk, system_prompt: Optional[str] = None, context_summaries: Optional[List[str]] = None) -> ChunkScore:
        """Score a single text chunk using Claude."""
        prompt = system_prompt or self.default_system_prompt
        
        # Build user message with context if available
        user_message = f"""Section: {chunk.section_name}"""
        
        # Add context from previous sections if available
        if context_summaries and self.use_context:
            user_message += f"""

Previous Sections Context:
"""
            for i, summary in enumerate(context_summaries[-3:], 1):  # Use last 3 summaries
                user_message += f"{i}. {summary}\n"
        
        user_message += f"""

Current Section Content:
{chunk.text}

Please evaluate this section considering the context from previous sections (if provided). Provide a score from 1-10 with reasoning and a brief summary."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1200,  # Increased for summary
                system=prompt,
                messages=[{"role": "user", "content": user_message}]
            )
            
            response_text = response.content[0].text
            score, reasoning, summary, detailed_scores = self._parse_response_with_detailed_scores(response_text)
            
            return ChunkScore(
                section_name=chunk.section_name,
                text=chunk.text,
                score=score,
                reasoning=reasoning,
                metadata={"model": self.model, "response": response_text, "summary": summary},
                detailed_scores=detailed_scores
            )
            
        except Exception as e:
            return ChunkScore(
                section_name=chunk.section_name,
                text=chunk.text,
                score=0.0,
                reasoning=f"Error during scoring: {str(e)}",
                metadata={"error": str(e), "summary": ""},
                detailed_scores=DetailedScores()
            )
    
    def score_chunks(self, chunks: List[TextChunk], 
                    system_prompt: Optional[str] = None,
                    delay_between_requests: float = 1.0) -> List[ChunkScore]:
        """Score multiple text chunks with rate limiting and context memory."""
        scores = []
        summaries = []  # Accumulate summaries for context
        
        for i, chunk in enumerate(chunks):
            if i > 0:
                time.sleep(delay_between_requests)
            
            # Score with context from previous sections
            score = self.score_chunk(chunk, system_prompt, summaries if self.use_context else None)
            scores.append(score)
            
            # Extract and store summary for future context
            summary = score.metadata.get("summary", "")
            if summary:
                section_summary = f"{chunk.section_name}: {summary}"
                summaries.append(section_summary)
            
        return scores
    
    def reset_context(self):
        """Reset the context memory (useful when starting a new paper)."""
        self.context_memory = []
    
    def _parse_response(self, response_text: str) -> tuple[float, str]:
        """Parse Claude's response to extract score and reasoning (legacy method)."""
        score, reasoning, _ = self._parse_response_with_summary(response_text)
        return score, reasoning
    
    def _parse_response_with_summary(self, response_text: str) -> tuple[float, str, str]:
        """Parse Claude's response to extract score, reasoning, and summary (legacy method)."""
        score, reasoning, summary, _ = self._parse_response_with_detailed_scores(response_text)
        return score, reasoning, summary

    def _parse_response_with_detailed_scores(self, response_text: str) -> tuple[float, str, str, DetailedScores]:
        """Parse Claude's response to extract score, reasoning, summary, and detailed scores."""
        try:
            import re
            lines = response_text.strip().split('\n')
            score = 0.0
            reasoning = ""
            summary = ""
            detailed_scores = DetailedScores()
            
            # Parse structured response
            current_section = None
            current_content = []
            in_detailed_scores = False
            
            for line in lines:
                line = line.strip()
                
                if line.lower().startswith('score:'):
                    score_text = line.split(':', 1)[1].strip()
                    score_match = re.search(r'(\d+(?:\.\d+)?)', score_text)
                    if score_match:
                        score = float(score_match.group(1))
                        score = max(1.0, min(10.0, score))
                    current_section = 'score'
                    in_detailed_scores = False
                    
                elif line.lower().startswith('detailed scores:'):
                    in_detailed_scores = True
                    current_section = 'detailed_scores'
                    
                elif in_detailed_scores and line.startswith('-'):
                    # Parse detailed score lines
                    score_line = line[1:].strip()  # Remove the dash
                    if 'clarity and writing quality:' in score_line.lower():
                        match = re.search(r'(\d+(?:\.\d+)?)', score_line)
                        if match:
                            detailed_scores.clarity_writing = float(match.group(1))
                    elif 'technical depth:' in score_line.lower():
                        match = re.search(r'(\d+(?:\.\d+)?)', score_line)
                        if match:
                            detailed_scores.technical_depth = float(match.group(1))
                    elif 'novelty and originality:' in score_line.lower():
                        match = re.search(r'(\d+(?:\.\d+)?)', score_line)
                        if match:
                            detailed_scores.novelty_originality = float(match.group(1))
                    elif 'methodology rigor:' in score_line.lower():
                        match = re.search(r'(\d+(?:\.\d+)?)', score_line)
                        if match:
                            detailed_scores.methodology_rigor = float(match.group(1))
                    elif 'evidence and support:' in score_line.lower():
                        match = re.search(r'(\d+(?:\.\d+)?)', score_line)
                        if match:
                            detailed_scores.evidence_support = float(match.group(1))
                    
                elif line.lower().startswith('reasoning:'):
                    in_detailed_scores = False
                    if current_section and current_content:
                        if current_section == 'score':
                            pass  # Already processed
                    reasoning = line.split(':', 1)[1].strip()
                    current_section = 'reasoning'
                    current_content = [reasoning] if reasoning else []
                    
                elif line.lower().startswith('summary:'):
                    in_detailed_scores = False
                    if current_section == 'reasoning' and current_content:
                        reasoning = ' '.join(current_content)
                    summary = line.split(':', 1)[1].strip()
                    current_section = 'summary'
                    current_content = [summary] if summary else []
                    
                elif line and current_section and not in_detailed_scores:
                    current_content.append(line)
            
            # Handle final section
            if current_section == 'reasoning' and current_content and not reasoning:
                reasoning = ' '.join(current_content)
            elif current_section == 'summary' and current_content and not summary:
                summary = ' '.join(current_content)
            
            # Fallbacks
            if not reasoning:
                reasoning = response_text.strip()
            if not summary:
                # Try to extract a brief summary from the reasoning
                sentences = reasoning.split('.')[:2]  # First 2 sentences
                summary = '.'.join(sentences).strip()
                if summary and not summary.endswith('.'):
                    summary += '.'
                
            return score, reasoning, summary, detailed_scores
            
        except Exception as e:
            return 5.0, f"Error parsing response: {str(e)}", "", DetailedScores()