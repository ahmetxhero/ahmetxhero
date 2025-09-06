#!/usr/bin/env python3
"""
Example Python Script for AhmetXHero Repository

This is a sample Python script demonstrating proper project structure.
"""

import argparse
import sys
from pathlib import Path


def main():
    """Main function to run the example script."""
    parser = argparse.ArgumentParser(description='Example Python script')
    parser.add_argument('--input', '-i', help='Input file path')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        print("Running example Python script...")
        print(f"Input: {args.input}")
        print(f"Output: {args.output}")
    
    # Example processing
    if args.input and Path(args.input).exists():
        print(f"Processing file: {args.input}")
        # Add your processing logic here
        if args.output:
            print(f"Results will be saved to: {args.output}")
    else:
        print("No valid input file provided")
        return 1
    
    print("Script completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
