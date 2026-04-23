#!/usr/bin/env python3
"""
Compile LaTeX document using multiple fallback methods:
1. Local pdflatex (preferred)
2. Docker container
3. Online service (ShareLaTeX/Overleaf API if available)
4. Convert to HTML/Markdown as last resort
"""

import os
import subprocess
import sys
import tempfile
import shutil
from pathlib import Path

def check_command(cmd):
    """Check if a command is available."""
    try:
        subprocess.run(["which", cmd], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def compile_with_pdflatex(tex_file):
    """Compile using local pdflatex."""
    print(f"Compiling with local pdflatex: {tex_file}")
    
    # Run pdflatex multiple times for references
    for i in range(3):
        print(f"  Pass {i+1}/3...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"  Warning: pdflatex returned {result.returncode}")
            if i == 0:  # First pass errors are more serious
                print("  First pass errors:")
                print(result.stderr[:500])
    
    pdf_file = tex_file.with_suffix('.pdf')
    if pdf_file.exists():
        size = pdf_file.stat().st_size / 1024  # KB
        print(f"✓ PDF created: {pdf_file} ({size:.1f} KB)")
        return True
    else:
        print("✗ PDF not created")
        return False

def compile_with_docker(tex_file):
    """Compile using Docker texlive image."""
    print("Compiling with Docker...")
    
    if not check_command("docker"):
        print("  Docker not available")
        return False
    
    # Get absolute path for volume mounting
    abs_path = tex_file.resolve()
    parent_dir = abs_path.parent
    
    try:
        # Run pdflatex in Docker container
        for i in range(3):
            print(f"  Docker pass {i+1}/3...")
            subprocess.run([
                "docker", "run", "--rm",
                "-v", f"{parent_dir}:/workspace",
                "texlive/texlive:latest",
                "pdflatex", "-interaction=nonstopmode",
                f"/workspace/{tex_file.name}"
            ], check=True, capture_output=True)
        
        pdf_file = tex_file.with_suffix('.pdf')
        if pdf_file.exists():
            size = pdf_file.stat().st_size / 1024
            print(f"✓ PDF created with Docker: {pdf_file} ({size:.1f} KB)")
            return True
        else:
            print("✗ Docker compilation failed")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"  Docker error: {e}")
        return False

def convert_to_html(tex_file):
    """Convert LaTeX to HTML as fallback."""
    print("Converting LaTeX to HTML (fallback)...")
    
    # Check for pandoc
    if not check_command("pandoc"):
        print("  pandoc not available for HTML conversion")
        return False
    
    html_file = tex_file.with_suffix('.html')
    try:
        subprocess.run([
            "pandoc", str(tex_file),
            "-o", str(html_file),
            "--mathjax",
            "--standalone"
        ], check=True, capture_output=True)
        
        if html_file.exists():
            size = html_file.stat().st_size / 1024
            print(f"✓ HTML created: {html_file} ({size:.1f} KB)")
            print(f"  Open with: firefox {html_file} or any browser")
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        print("  pandoc conversion failed")
        return False

def create_readable_text(tex_file):
    """Create a readable text version by extracting content."""
    print("Creating readable text version...")
    
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple extraction: remove LaTeX commands, keep text
        import re
        
        # Remove \begin{...} ... \end{...}
        content = re.sub(r'\\begin\{.*?\}.*?\\end\{.*?\}', '', content, flags=re.DOTALL)
        
        # Remove commands starting with \
        content = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', content)
        content = re.sub(r'\\[a-zA-Z]+', '', content)
        
        # Remove comments
        content = re.sub(r'%.*', '', content)
        
        # Clean up extra whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        text_file = tex_file.with_suffix('.txt')
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write("# Readable Text Version of LaTeX Document\n\n")
            f.write(content)
        
        print(f"✓ Text version created: {text_file}")
        return True
        
    except Exception as e:
        print(f"  Error creating text version: {e}")
        return False

def main():
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    tex_file = Path("complete_derivations.tex")
    
    if not tex_file.exists():
        print(f"Error: {tex_file} not found")
        print(f"Current directory: {os.getcwd()}")
        return 1
    
    print(f"=== Compiling LaTeX Document ===")
    print(f"Document: {tex_file}")
    print(f"Size: {tex_file.stat().st_size / 1024:.1f} KB")
    print()
    
    # Method 1: Local pdflatex
    if check_command("pdflatex"):
        if compile_with_pdflatex(tex_file):
            return 0
        print()
    
    # Method 2: Docker
    print("--- Trying Docker ---")
    if compile_with_docker(tex_file):
        return 0
    print()
    
    # Method 3: HTML conversion
    print("--- Creating HTML version ---")
    if convert_to_html(tex_file):
        print("\nHTML version created as fallback.")
        print("You can view it in any web browser.")
        return 0
    print()
    
    # Method 4: Simple text extraction
    print("--- Creating text version ---")
    if create_readable_text(tex_file):
        print("\nText version created as last resort.")
        print("This contains the content without LaTeX formatting.")
        return 0
    
    print("\n=== All compilation methods failed ===")
    print("Options:")
    print("1. Install LaTeX: sudo dnf install texlive texlive-amsmath texlive-physics")
    print("2. Install Docker and run: ./compile_with_docker.sh")
    print("3. Use online LaTeX editor (Overleaf.com)")
    print("4. Copy the .tex file to a system with LaTeX installed")
    return 1

if __name__ == "__main__":
    sys.exit(main())