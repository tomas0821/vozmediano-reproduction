#!/bin/bash

# Script to compile the LaTeX document for Vozmediano et al. derivations

set -e  # Exit on error

echo "=== LaTeX Compilation Script ==="
echo "Document: complete_derivations.tex"
echo ""

# Check if we're in the right directory
if [ ! -f "complete_derivations.tex" ]; then
    echo "Error: complete_derivations.tex not found in current directory"
    echo "Please run this script from the repro_vozmediano_0807_3909 directory"
    exit 1
fi

# Check if LaTeX is installed
if ! command -v pdflatex &> /dev/null; then
    echo "LaTeX (pdflatex) not found. Attempting to install..."
    
    # Check if we have sudo access
    if [ "$EUID" -eq 0 ]; then
        echo "Running as root, installing texlive packages..."
        dnf install -y texlive texlive-amsmath texlive-amssymb texlive-amsthm \
            texlive-graphics texlive-hyperref texlive-geometry texlive-booktabs \
            texlive-physics texlive-siunitx texlive-latexmk
    else
        echo "Please run with sudo or ask your system administrator to install:"
        echo "  texlive texlive-amsmath texlive-amssymb texlive-amsthm"
        echo "  texlive-graphics texlive-hyperref texlive-geometry texlive-booktabs"
        echo "  texlive-physics texlive-siunitx texlive-latexmk"
        exit 1
    fi
fi

# Check for required packages
echo "Checking LaTeX installation..."
if ! pdflatex --version &> /dev/null; then
    echo "pdflatex is not working properly after installation"
    exit 1
fi

echo "LaTeX is installed. Starting compilation..."

# First pass - generate aux files and table of contents
echo "=== First pass (generating aux files) ==="
pdflatex -interaction=nonstopmode complete_derivations.tex

# Second pass - resolve references
echo "=== Second pass (resolving references) ==="
pdflatex -interaction=nonstopmode complete_derivations.tex

# Third pass - final compilation
echo "=== Third pass (final compilation) ==="
pdflatex -interaction=nonstopmode complete_derivations.tex

# Check if PDF was created
if [ -f "complete_derivations.pdf" ]; then
    echo ""
    echo "=== SUCCESS ==="
    echo "PDF created: complete_derivations.pdf"
    echo "File size: $(du -h complete_derivations.pdf | cut -f1)"
    
    # Create a simple HTML preview if pandoc is available
    if command -v pandoc &> /dev/null; then
        echo "Creating HTML preview..."
        pandoc complete_derivations.tex -o complete_derivations_preview.html --mathjax
        echo "HTML preview created: complete_derivations_preview.html"
    fi
else
    echo ""
    echo "=== WARNING ==="
    echo "PDF was not created. Check the log file for errors."
    echo "You can try running: pdflatex complete_derivations.tex"
fi

echo ""
echo "=== Compilation complete ==="