#!/usr/bin/env python3
"""
Helper script for creating perfect PDF from HTML with MathJax equations.
"""

import sys
import os
import webbrowser
import time
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    html_file = Path("complete_derivations.html")
    
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        return 1
    
    print("=" * 60)
    print("PERFECT PDF CREATION HELPER")
    print("=" * 60)
    print()
    print("This script helps you create a perfect PDF with all equations")
    print("correctly rendered using your web browser.")
    print()
    print(f"HTML file: {html_file}")
    print(f"File size: {html_file.stat().st_size / 1024:.1f} KB")
    print()
    
    print("STEP 1: Open the HTML file in your browser")
    print("-" * 40)
    print()
    
    # Try to open the file
    print("Attempting to open in default browser...")
    try:
        webbrowser.open(f"file://{html_file.resolve()}")
        print("✅ Browser opened (or opening)")
    except Exception as e:
        print(f"⚠️  Could not open automatically: {e}")
        print(f"   Please open manually: {html_file}")
    
    print()
    print("STEP 2: Wait for equations to render")
    print("-" * 40)
    print()
    print("IMPORTANT: Wait 10-15 seconds for MathJax to render all equations.")
    print("You should see equations change from LaTeX code to proper math symbols.")
    print()
    
    # Countdown
    print("Waiting time (you can continue manually):")
    for i in range(10, 0, -1):
        print(f"  {i} seconds...")
        time.sleep(1)
    
    print()
    print("STEP 3: Print to PDF")
    print("-" * 40)
    print()
    print("INSTRUCTIONS FOR DIFFERENT BROWSERS:")
    print()
    
    print("CHROME/CHROMIUM:")
    print("  1. Press Ctrl+P (or Cmd+P on Mac)")
    print("  2. Destination: Select 'Save as PDF'")
    print("  3. Settings:")
    print("     - Layout: Portrait")
    print("     - Paper size: Letter or A4")
    print("     - Margins: Default")
    print("     - Scale: 100%")
    print("     - ☑ Background graphics")
    print("  4. Click 'Save'")
    print("  5. Save as: complete_derivations_perfect.pdf")
    print()
    
    print("FIREFOX:")
    print("  1. Press Ctrl+P (or Cmd+P on Mac)")
    print("  2. Printer: Select 'Microsoft Print to PDF' or similar")
    print("  3. More settings:")
    print("     - Format: PDF")
    print("     - Scale: 100%")
    print("     - ☑ Print backgrounds")
    print("  4. Click 'Save'")
    print()
    
    print("SAFARI:")
    print("  1. Press Cmd+P")
    print("  2. Click 'PDF' dropdown → 'Save as PDF'")
    print("  3. Adjust settings if needed")
    print("  4. Click 'Save'")
    print()
    
    print("STEP 4: Verify the PDF")
    print("-" * 40)
    print()
    print("Open the PDF and check:")
    print("  ✅ All equations are properly rendered")
    print("  ✅ No missing symbols or Greek letters")
    print("  ✅ Formatting looks correct")
    print()
    
    print("TROUBLESHOOTING:")
    print("-" * 40)
    print()
    print("If equations don't render in PDF:")
    print("  1. Wait longer before printing (MathJax needs time)")
    print("  2. Scroll through the entire document first")
    print("  3. Try a different browser")
    print("  4. Check internet connection (MathJax uses CDN)")
    print()
    
    print("ALTERNATIVE: Command line with Chrome")
    print("-" * 40)
    print()
    print("If you have Chrome/Chromium installed, try:")
    print(f"  google-chrome --headless --disable-gpu \\")
    print(f"    --print-to-pdf=complete_derivations_chrome.pdf \\")
    print(f"    --run-all-compositor-stages-before-draw \\")
    print(f"    --virtual-time-budget=10000 \\")
    print(f"    file://$(pwd)/{html_file}")
    print()
    print("Note: This may still have timing issues with MathJax.")
    print()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print()
    print("The browser print-to-PDF method is the MOST RELIABLE way")
    print("to get perfect equations without LaTeX installation.")
    print()
    print("Files available:")
    print(f"  - {html_file}: HTML with MathJax (best for viewing)")
    print(f"  - complete_derivations.tex: LaTeX source")
    print(f"  - complete_derivations_latex_source.pdf: LaTeX code PDF")
    print()
    print("After following these steps, you should have:")
    print(f"  - complete_derivations_perfect.pdf: Perfect PDF with equations")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())