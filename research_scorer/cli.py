"""Command-line interface for the research paper scorer."""

import json
import os
from pathlib import Path
from typing import Optional

import click
from dotenv import load_dotenv

from .paper_scorer import PaperScorer


@click.group()
def cli():
    """Research Paper Scoring CLI"""
    load_dotenv()


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--api-key', help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
@click.option('--model', default='claude-3-5-haiku-20241022', help='Claude model to use')
@click.option('--output', '-o', help='Output JSON file for results')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--save-markdown/--no-save-markdown', default=True, help='Save detailed results as markdown')
@click.option('--results-dir', default='results', help='Directory to save markdown results')
@click.option('--use-context/--no-use-context', default=True, help='Use contextual memory from previous sections')
def score(pdf_path: str, api_key: Optional[str], model: str, output: Optional[str], verbose: bool, save_markdown: bool, results_dir: str, use_context: bool):
    """Score a single research paper."""
    
    # Get API key from environment if not provided
    if not api_key:
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            click.echo("Error: API key required. Set ANTHROPIC_API_KEY or use --api-key", err=True)
            return
    
    try:
        scorer = PaperScorer(
            api_key=api_key, 
            model=model, 
            save_detailed_results=save_markdown,
            results_dir=results_dir,
            use_context=use_context
        )
        result = scorer.score_paper(pdf_path)
        
        if verbose:
            click.echo(f"Paper: {result.paper_path}")
            click.echo(f"Average Score: {result.average_score:.2f}")
            click.echo(f"Total Chunks: {result.total_chunks}")
            click.echo(f"Processing Time: {result.processing_time:.2f}s")
            click.echo("\nSection Scores:")
            for chunk_score in result.chunk_scores:
                click.echo(f"  {chunk_score.section_name}: {chunk_score.score:.1f}")
        else:
            click.echo(f"Score: {result.average_score:.2f}")
        
        if output:
            output_data = {
                "paper_path": result.paper_path,
                "average_score": result.average_score,
                "total_chunks": result.total_chunks,
                "processing_time": result.processing_time,
                "chunk_scores": [
                    {
                        "section_name": cs.section_name,
                        "score": cs.score,
                        "reasoning": cs.reasoning
                    }
                    for cs in result.chunk_scores
                ]
            }
            
            with open(output, 'w') as f:
                json.dump(output_data, f, indent=2)
            click.echo(f"Results saved to: {output}")
            
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@cli.command()
@click.argument('papers_dir', type=click.Path(exists=True))
@click.option('--api-key', help='Anthropic API key (or set ANTHROPIC_API_KEY env var)')
@click.option('--model', default='claude-3-5-haiku-20241022', help='Claude model to use')
@click.option('--output', '-o', help='Output JSON file for results')
@click.option('--pattern', default='*.pdf', help='File pattern to match')
@click.option('--save-markdown/--no-save-markdown', default=True, help='Save detailed results as markdown')
@click.option('--results-dir', default='results', help='Directory to save markdown results')
@click.option('--use-context/--no-use-context', default=True, help='Use contextual memory from previous sections')
def batch(papers_dir: str, api_key: Optional[str], model: str, output: Optional[str], pattern: str, save_markdown: bool, results_dir: str, use_context: bool):
    """Score multiple papers in a directory."""
    
    if not api_key:
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            click.echo("Error: API key required. Set ANTHROPIC_API_KEY or use --api-key", err=True)
            return
    
    try:
        # Find all PDF files
        papers_path = Path(papers_dir)
        pdf_files = list(papers_path.glob(pattern))
        
        if not pdf_files:
            click.echo(f"No PDF files found in {papers_dir} matching {pattern}")
            return
        
        click.echo(f"Found {len(pdf_files)} PDF files")
        
        scorer = PaperScorer(
            api_key=api_key, 
            model=model,
            save_detailed_results=save_markdown,
            results_dir=results_dir,
            use_context=use_context
        )
        results = scorer.batch_process_with_markdown([str(f) for f in pdf_files])
        
        # Display summary
        summary = scorer.get_summary_report(results)
        click.echo(f"\nProcessed {summary['total_papers']} papers")
        click.echo(f"Average Score: {summary['average_score']:.2f}")
        click.echo(f"Highest Score: {summary['highest_score']:.2f}")
        click.echo(f"Lowest Score: {summary['lowest_score']:.2f}")
        
        # Show individual results
        click.echo("\nIndividual Results:")
        for paper in summary['papers']:
            paper_name = Path(paper['path']).name
            click.echo(f"  {paper_name}: {paper['score']:.2f}")
        
        if output:
            with open(output, 'w') as f:
                json.dump(summary, f, indent=2)
            click.echo(f"\nResults saved to: {output}")
            
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


if __name__ == '__main__':
    cli()