#!/bin/bash

# Script to view the document in the preferred format

echo "=== View Vozmediano Derivations Document ==="
echo ""

# Check what files are available
if [ -f "complete_derivations.html" ]; then
    echo "✅ HTML version available (34.0 KB)"
    HTML_AVAILABLE=true
else
    echo "❌ HTML version not found"
    HTML_AVAILABLE=false
fi

if [ -f "complete_derivations.pdf" ]; then
    PDF_SIZE=$(du -h complete_derivations.pdf | cut -f1)
    echo "✅ PDF version available ($PDF_SIZE)"
    PDF_AVAILABLE=true
else
    echo "❌ PDF version not found (compile to create)"
    PDF_AVAILABLE=false
fi

echo ""
echo "Available viewing options:"

if [ "$HTML_AVAILABLE" = true ]; then
    echo "1. View HTML in browser (recommended)"
fi

if [ "$PDF_AVAILABLE" = true ]; then
    echo "2. View PDF"
fi

echo "3. View LaTeX source"
echo "4. Open compilation guide"
echo ""

read -p "Choose option (1-4): " choice

case $choice in
    1)
        if [ "$HTML_AVAILABLE" = true ]; then
            echo "Opening HTML in browser..."
            xdg-open complete_derivations.html 2>/dev/null || \
            echo "Please open: complete_derivations.html"
        else
            echo "HTML not available. Try: pandoc complete_derivations.tex -o complete_derivations.html --mathjax"
        fi
        ;;
    2)
        if [ "$PDF_AVAILABLE" = true ]; then
            echo "Opening PDF..."
            xdg-open complete_derivations.pdf 2>/dev/null || \
            echo "Please open: complete_derivations.pdf"
        else
            echo "PDF not available. Compile first using:"
            echo "  ./compile_latex.py"
            echo "  or upload to overleaf.com"
        fi
        ;;
    3)
        echo "Showing LaTeX source (first 50 lines)..."
        head -50 complete_derivations.tex
        echo ""
        echo "Full file: complete_derivations.tex (21.8 KB)"
        ;;
    4)
        echo "Opening compilation guide..."
        cat README_COMPILATION.md
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

echo ""
echo "For more options, see:"
echo "  README_COMPILATION.md - Quick start guide"
echo "  COMPILATION_GUIDE.md - Detailed compilation methods"