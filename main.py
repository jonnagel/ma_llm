"""
Entry point for multi-agent bias mitigation framework.
"""

import argparse
import json
from typing import List
from multi_agent_dialectic import MultiAgentDialectic, CultureScore


def main():
    """
    Execute multi-agent evaluation based on command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Multi-Agent LLM Framework for Bias Mitigation & Decision Risk Reduction'
    )
    parser.add_argument(
        '--target',
        type=str,
        required=True,
        help='Search query (e.g., "Chicago healthcare data roles")'
    )
    parser.add_argument(
        '--companies',
        nargs='+',
        help='Specific companies to evaluate'
    )
    parser.add_argument(
        '--min-coherence',
        type=float,
        default=60.0,
        help='Minimum coherence score threshold (default: 60)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='evaluation_results.json',
        help='Output file for results'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Initialize the multi-agent system
    dialectic_system = MultiAgentDialectic()
    
    # Evaluate companies
    if args.companies:
        scores = dialectic_system.batch_evaluate(args.companies)
    else:
        # Auto-discover companies based on target query
        pass
    
    # Filter by minimum coherence
    qualified_scores = [s for s in scores if s.coherence_score >= args.min_coherence]
    
    # Generate report
    report = dialectic_system.generate_report(qualified_scores)
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump([s.__dict__ for s in qualified_scores], f, indent=2)
    
    if args.verbose:
        print(report)
    else:
        print(f"Evaluated {len(scores)} companies")
        print(f"Found {len(qualified_scores)} matches above {args.min_coherence} threshold")
        print(f"Results saved to {args.output}")


if __name__ == '__main__':
    main()

