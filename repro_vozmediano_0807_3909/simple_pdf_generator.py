#!/usr/bin/env python3
"""
Simple PDF generator using reportlab for basic PDF creation.
This won't preserve complex LaTeX formatting but will create a readable PDF.
"""

import sys
from pathlib import Path
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False

def extract_text_from_html(html_file):
    """Extract readable text from HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple HTML stripping - remove tags, keep text
    import re
    
    # Remove script and style tags
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    
    # Remove HTML tags but keep text
    content = re.sub(r'<[^>]+>', ' ', content)
    
    # Decode HTML entities
    import html
    content = html.unescape(content)
    
    # Clean up whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content

def create_simple_pdf(text, pdf_file):
    """Create a simple PDF with the text."""
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        textColor=colors.HexColor('#1a237e')
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor=colors.HexColor('#283593')
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        leading=14
    )
    
    # Build story
    story = []
    
    # Title
    story.append(Paragraph("Complete Derivations for", title_style))
    story.append(Paragraph("Gauge fields and curvature in graphene", title_style))
    story.append(Paragraph("Vozmediano et al. (2008), arXiv:0807.3909", styles['Heading2']))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Italic']))
    story.append(Spacer(1, 0.5*inch))
    
    # Process text
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if it's a heading
        if line.startswith('# ') or 'Introduction' in line:
            story.append(Paragraph(line.replace('# ', ''), heading_style))
        elif any(line.startswith(x) for x in ['## ', '### ', '#### ']):
            # Subheadings
            clean_line = line.lstrip('# ')
            story.append(Paragraph(clean_line, styles['Heading3']))
        else:
            # Normal text
            story.append(Paragraph(line, normal_style))
        
        story.append(Spacer(1, 0.1*inch))
    
    # Build PDF
    doc.build(story)
    return True

def main():
    # Check for reportlab
    if not HAS_REPORTLAB:
        print("Error: reportlab library not installed.")
        print("Install with: pip install reportlab")
        print("\nAlternative: Use browser print-to-PDF:")
        print("1. Open complete_derivations.html in browser")
        print("2. Press Ctrl+P")
        print("3. Choose 'Save as PDF'")
        return 1
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    html_file = Path("complete_derivations.html")
    pdf_file = Path("complete_derivations_simple.pdf")
    
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        return 1
    
    print(f"Creating simple PDF from HTML...")
    print(f"Source: {html_file}")
    
    try:
        # Extract text
        text = extract_text_from_html(html_file)
        
        # Create PDF
        if create_simple_pdf(text, pdf_file):
            size = pdf_file.stat().st_size / 1024
            print(f"✅ Simple PDF created: {pdf_file} ({size:.1f} KB)")
            print(f"   Note: This is a basic text PDF without LaTeX equations.")
            print(f"   For full formatting, use Overleaf or install LaTeX.")
            return 0
        else:
            print("✗ Failed to create PDF")
            return 1
            
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    import os
    sys.exit(main())