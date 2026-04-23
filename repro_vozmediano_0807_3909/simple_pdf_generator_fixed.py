#!/usr/bin/env python3
"""
Simple PDF generator using reportlab for basic PDF creation.
"""

import sys
import os
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
    
    # Simple HTML stripping
    import re
    import html
    
    # Remove script and style tags
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    
    # Remove HTML tags but keep text
    content = re.sub(r'<[^>]+>', ' ', content)
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Clean up whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content

def create_simple_pdf(text, pdf_path):
    """Create a simple PDF with the text."""
    # Convert Path to string
    pdf_file = str(pdf_path)
    
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
    
    # Process text (take first 5000 chars to keep PDF small)
    text_preview = text[:5000] + "..." if len(text) > 5000 else text
    
    # Split into paragraphs
    paragraphs = text_preview.split('\n\n')
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Simple heading detection
        if 'Introduction' in para or 'Mathematical Preliminaries' in para:
            story.append(Paragraph(para, heading_style))
        elif len(para) < 100 and para.endswith(':'):
            # Likely a heading
            story.append(Paragraph(para, styles['Heading3']))
        else:
            # Normal text
            story.append(Paragraph(para, normal_style))
        
        story.append(Spacer(1, 0.05*inch))
    
    # Add note about full content
    story.append(PageBreak())
    story.append(Paragraph("Note:", heading_style))
    story.append(Paragraph("This is a simplified text version of the document.", normal_style))
    story.append(Paragraph("For the full document with mathematical equations:", normal_style))
    story.append(Paragraph("1. View complete_derivations.html in a web browser", normal_style))
    story.append(Paragraph("2. Use Overleaf (overleaf.com) to compile the LaTeX", normal_style))
    story.append(Paragraph("3. Install LaTeX locally for full PDF generation", normal_style))
    
    # Build PDF
    doc.build(story)
    return True

def main():
    # Check for reportlab
    if not HAS_REPORTLAB:
        print("Error: reportlab library not installed.")
        print("Install with: pip install reportlab")
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
        print(f"  Extracted {len(text)} characters")
        
        # Create PDF
        print("  Generating PDF...")
        if create_simple_pdf(text, pdf_file):
            size = pdf_file.stat().st_size / 1024
            print(f"✅ Simple PDF created: {pdf_file} ({size:.1f} KB)")
            print(f"   Note: This is a basic text PDF without LaTeX equations.")
            print(f"   For full formatting:")
            print(f"   1. Open {html_file} in browser for equations")
            print(f"   2. Use Overleaf.com for full LaTeX PDF")
            return 0
        else:
            print("✗ Failed to create PDF")
            return 1
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())