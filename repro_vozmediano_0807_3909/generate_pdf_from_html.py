#!/usr/bin/env python3
"""
Generate PDF from HTML using multiple fallback methods.
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

def check_command(cmd):
    """Check if a command is available."""
    try:
        subprocess.run(["which", cmd], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def pdf_with_wkhtmltopdf(html_file, pdf_file):
    """Generate PDF using wkhtmltopdf."""
    print("Trying wkhtmltopdf...")
    try:
        subprocess.run([
            "wkhtmltopdf",
            "--enable-local-file-access",
            "--page-size", "A4",
            "--margin-top", "20mm",
            "--margin-bottom", "20mm",
            "--margin-left", "20mm",
            "--margin-right", "20mm",
            html_file,
            pdf_file
        ], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def pdf_with_weasyprint(html_file, pdf_file):
    """Generate PDF using weasyprint."""
    print("Trying weasyprint...")
    try:
        subprocess.run([
            "weasyprint",
            html_file,
            pdf_file
        ], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def pdf_with_pandoc(html_file, pdf_file):
    """Generate PDF using pandoc (requires LaTeX)."""
    print("Trying pandoc to PDF...")
    try:
        subprocess.run([
            "pandoc",
            html_file,
            "-o", pdf_file,
            "--pdf-engine=xelatex"
        ], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def pdf_with_chrome(headless_chrome_cmd, html_file, pdf_file):
    """Generate PDF using headless Chrome/Chromium."""
    print(f"Trying {headless_chrome_cmd}...")
    
    # Create a simple HTML file that loads the actual file
    # Chrome needs a file:// URL or local server
    abs_html_path = Path(html_file).resolve()
    
    try:
        subprocess.run([
            headless_chrome_cmd,
            "--headless",
            "--disable-gpu",
            "--print-to-pdf=" + str(pdf_file),
            "file://" + str(abs_html_path)
        ], check=True, capture_output=True, timeout=30)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False

def install_wkhtmltopdf():
    """Try to install wkhtmltopdf."""
    print("Attempting to install wkhtmltopdf...")
    try:
        # Try different package managers
        if check_command("dnf"):
            print("  Using dnf (Fedora/RHEL)...")
            subprocess.run(["sudo", "dnf", "install", "-y", "wkhtmltopdf"], 
                         capture_output=True)
        elif check_command("apt"):
            print("  Using apt (Debian/Ubuntu)...")
            subprocess.run(["sudo", "apt", "update"], capture_output=True)
            subprocess.run(["sudo", "apt", "install", "-y", "wkhtmltopdf"], 
                         capture_output=True)
        elif check_command("yum"):
            print("  Using yum (CentOS)...")
            subprocess.run(["sudo", "yum", "install", "-y", "wkhtmltopdf"], 
                         capture_output=True)
        else:
            print("  No supported package manager found")
            return False
        
        # Check if installation succeeded
        if check_command("wkhtmltopdf"):
            print("  ✓ wkhtmltopdf installed successfully")
            return True
        else:
            print("  ✗ Installation failed")
            return False
            
    except Exception as e:
        print(f"  Installation error: {e}")
        return False

def main():
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    html_file = Path("complete_derivations.html")
    pdf_file = Path("complete_derivations_from_html.pdf")
    
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        print("First generate HTML with: python3 compile_latex.py")
        return 1
    
    print(f"=== Generating PDF from HTML ===")
    print(f"Source: {html_file} ({html_file.stat().st_size / 1024:.1f} KB)")
    print()
    
    # Try multiple methods
    methods = [
        ("wkhtmltopdf", lambda: pdf_with_wkhtmltopdf(html_file, pdf_file)),
        ("weasyprint", lambda: pdf_with_weasyprint(html_file, pdf_file)),
        ("pandoc", lambda: pdf_with_pandoc(html_file, pdf_file)),
        ("chrome", lambda: pdf_with_chrome("google-chrome", html_file, pdf_file)),
        ("chromium", lambda: pdf_with_chrome("chromium-browser", html_file, pdf_file)),
    ]
    
    success = False
    for name, method in methods:
        print(f"Method: {name}")
        if method():
            success = True
            break
        print()
    
    if not success:
        print("All PDF generation methods failed.")
        print("\nOptions:")
        print("1. Install wkhtmltopdf:")
        print("   sudo dnf install wkhtmltopdf  # Fedora/RHEL")
        print("   sudo apt install wkhtmltopdf  # Debian/Ubuntu")
        print()
        print("2. Use Overleaf (online):")
        print("   - Go to overleaf.com")
        print("   - Upload complete_derivations.tex")
        print("   - Download PDF")
        print()
        print("3. Print HTML to PDF from browser:")
        print("   - Open complete_derivations.html in browser")
        print("   - Ctrl+P → Save as PDF")
        return 1
    
    if pdf_file.exists():
        size = pdf_file.stat().st_size / 1024
        print(f"\n✅ PDF created: {pdf_file} ({size:.1f} KB)")
        print(f"   Open with: xdg-open {pdf_file}")
        return 0
    else:
        print("\n✗ PDF file was not created")
        return 1

if __name__ == "__main__":
    sys.exit(main())