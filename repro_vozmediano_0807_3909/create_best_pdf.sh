#!/bin/bash

# Create the best possible PDF given system constraints

set -e

echo "=== Creating Best Possible PDF ==="
echo ""

cd "$(dirname "$0")"

# Check what's available
HTML_PDF="complete_derivations_simple.pdf"
HTML_FILE="complete_derivations.html"
TEX_FILE="complete_derivations.tex"

echo "Available files:"
echo "  - $TEX_FILE (LaTeX source, 21.8 KB)"
echo "  - $HTML_FILE (HTML with MathJax, 34.0 KB)"
echo "  - $HTML_PDF (Simple text PDF, 6.3 KB)"

echo ""
echo "Options for PDF creation:"

echo "1. ✅ Use existing simple PDF (fastest)"
echo "   $HTML_PDF - Basic text version"

echo "2. 🔄 Create improved PDF from HTML (recommended)"
echo "   Uses browser print-to-PDF for better formatting"

echo "3. 🌐 Use Overleaf online (best quality)"
echo "   Upload $TEX_FILE to overleaf.com"

echo "4. 🐳 Use Docker (if available)"
echo "   Runs: ./compile_with_docker.sh"

echo "5. 📄 Install LaTeX locally (permanent solution)"
echo "   Runs: ./compile_latex.sh"

echo ""
read -p "Choose option (1-5): " choice

case $choice in
    1)
        echo "Using existing simple PDF..."
        if [ -f "$HTML_PDF" ]; then
            echo "✅ Opening: $HTML_PDF"
            xdg-open "$HTML_PDF" 2>/dev/null || echo "Open manually: $HTML_PDF"
        else
            echo "❌ $HTML_PDF not found"
            echo "Run: python3 simple_pdf_generator_fixed.py"
        fi
        ;;
    2)
        echo "Creating improved PDF from HTML..."
        echo ""
        echo "INSTRUCTIONS:"
        echo "1. Open $HTML_FILE in your web browser"
        echo "2. Wait for MathJax to load equations (5-10 seconds)"
        echo "3. Press Ctrl+P (or Cmd+P on Mac)"
        echo "4. Choose 'Save as PDF' as printer"
        echo "5. Adjust margins if needed"
        echo "6. Save as 'complete_derivations_browser.pdf'"
        echo ""
        echo "This will preserve equations and formatting better than the simple PDF."
        
        # Try to open the HTML file
        if [ -f "$HTML_FILE" ]; then
            read -p "Open HTML in browser now? (y/n): " open_browser
            if [[ "$open_browser" =~ ^[Yy]$ ]]; then
                xdg-open "$HTML_FILE" 2>/dev/null || \
                echo "Please open manually: $HTML_FILE"
            fi
        fi
        ;;
    3)
        echo "Using Overleaf online..."
        echo ""
        echo "STEPS:"
        echo "1. Go to https://www.overleaf.com"
        echo "2. Create account/login (free)"
        echo "3. Click 'New Project' → 'Upload Project'"
        echo "4. Select $TEX_FILE"
        echo "5. Wait for compilation"
        echo "6. Download PDF"
        echo ""
        echo "Benefits:"
        echo "  - Perfect LaTeX compilation"
        echo "  - No installation needed"
        echo "  - Collaborative features"
        ;;
    4)
        echo "Using Docker..."
        if command -v docker &> /dev/null; then
            echo "Docker found. Running compilation..."
            ./compile_with_docker.sh
        else
            echo "❌ Docker not installed"
            echo "Install Docker or use another option"
        fi
        ;;
    5)
        echo "Installing LaTeX locally..."
        echo "This requires sudo access."
        echo ""
        read -p "Continue with installation? (y/n): " install_choice
        if [[ "$install_choice" =~ ^[Yy]$ ]]; then
            ./compile_latex.sh
        else
            echo "Installation cancelled"
        fi
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

echo ""
echo "=== Summary ==="
echo "For immediate use: Option 1 (simple PDF) or 2 (browser print)"
echo "For best quality: Option 3 (Overleaf)"
echo "For future work: Option 5 (install LaTeX)"