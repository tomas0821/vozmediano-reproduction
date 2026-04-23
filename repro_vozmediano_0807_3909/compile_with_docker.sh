#!/bin/bash

# Script to compile LaTeX using Docker (no local LaTeX installation needed)

set -e

echo "=== Docker LaTeX Compilation ==="
echo "Using texlive/texlive:latest Docker image"
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Please install Docker or use the local compilation script."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "complete_derivations.tex" ]; then
    echo "Error: complete_derivations.tex not found in current directory"
    echo "Please run this script from the repro_vozmediano_0807_3909 directory"
    exit 1
fi

echo "Starting Docker container with texlive..."
echo "This may take a minute to download the image on first run..."

# Run pdflatex in a Docker container
docker run --rm -v "$(pwd):/workspace" texlive/texlive:latest \
    pdflatex -interaction=nonstopmode /workspace/complete_derivations.tex

# Run second pass for references
docker run --rm -v "$(pwd):/workspace" texlive/texlive:latest \
    pdflatex -interaction=nonstopmode /workspace/complete_derivations.tex

# Run third pass for final compilation
docker run --rm -v "$(pwd):/workspace" texlive/texlive:latest \
    pdflatex -interaction=nonstopmode /workspace/complete_derivations.tex

# Check if PDF was created
if [ -f "complete_derivations.pdf" ]; then
    echo ""
    echo "=== SUCCESS ==="
    echo "PDF created: complete_derivations.pdf"
    echo "File size: $(du -h complete_derivations.pdf | cut -f1)"
else
    echo ""
    echo "=== ERROR ==="
    echo "PDF was not created. Check for LaTeX errors above."
fi