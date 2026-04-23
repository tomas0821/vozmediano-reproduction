#!/usr/bin/env python3
"""
Create a PDF that preserves LaTeX source code with syntax highlighting.
This is useful when equation rendering fails - at least you can see the actual LaTeX.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.lib import colors
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False

def read_latex_with_line_numbers(tex_file):
    """Read LaTeX file and add line numbers."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Add line numbers
    numbered_lines = []
    for i, line in enumerate(lines, 1):
        # Truncate very long lines
        if len(line) > 200:
            line = line[:197] + "...\n"
        numbered_lines.append(f"{i:4d}: {line}")
    
    return "".join(numbered_lines)

def extract_important_sections(tex_content):
    """Extract important sections (equations, theorems, etc.) from LaTeX."""
    sections = []
    
    # Find equation environments
    import re
    
    # Equation patterns
    patterns = [
        (r'\\begin\{equation\}(.*?)\\end\{equation\}', 'Equation'),
        (r'\\begin\{align\}(.*?)\\end\{align\}', 'Align'),
        (r'\\begin\{eqnarray\}(.*?)\\end\{eqnarray\}', 'Eqnarray'),
        (r'\\begin\{theorem\}(.*?)\\end\{theorem\}', 'Theorem'),
        (r'\\begin\{proof\}(.*?)\\end\{proof\}', 'Proof'),
        (r'\\begin\{definition\}(.*?)\\end\{definition\}', 'Definition'),
    ]
    
    for pattern, label in patterns:
        matches = re.finditer(pattern, tex_content, re.DOTALL)
        for match in matches:
            content = match.group(1).strip()
            # Clean up: remove line breaks in equations
            content = re.sub(r'\s+', ' ', content)
            sections.append({
                'type': label,
                'content': content[:500] + ("..." if len(content) > 500 else "")
            })
    
    # Also get section headings
    section_matches = re.finditer(r'\\(section|subsection|subsubsection)\{([^}]+)\}', tex_content)
    for match in section_matches:
        sections.append({
            'type': match.group(1).capitalize(),
            'content': match.group(2)
        })
    
    return sections

def create_latex_source_pdf(tex_file, pdf_file):
    """Create PDF with LaTeX source code."""
    # Read LaTeX content
    with open(tex_file, 'r', encoding='utf-8') as f:
        tex_content = f.read()
    
    # Extract important sections
    important_sections = extract_important_sections(tex_content)
    
    # Create PDF
    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=24,
        textColor=colors.HexColor('#1a237e'),
        alignment=1  # Center
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor=colors.HexColor('#283593')
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        spaceAfter=6,
        leading=11,
        textColor=colors.HexColor('#2e7d32'),
        leftIndent=20,
        rightIndent=20
    )
    
    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        leading=13
    )
    
    # Build story
    story = []
    
    # Title page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("LaTeX Source Code", title_style))
    story.append(Paragraph("Complete Derivations for", styles['Heading2']))
    story.append(Paragraph("Gauge fields and curvature in graphene", styles['Heading2']))
    story.append(Paragraph("Vozmediano et al. (2008), arXiv:0807.3909", styles['Heading3']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Italic']))
    story.append(Paragraph("This PDF contains the LaTeX source code.", styles['Italic']))
    story.append(Paragraph("For rendered equations, use the HTML file.", styles['Italic']))
    story.append(PageBreak())
    
    # Important sections
    story.append(Paragraph("Important Equations and Sections", section_style))
    story.append(Spacer(1, 0.25*inch))
    
    for i, section in enumerate(important_sections[:50]):  # Limit to first 50
        story.append(Paragraph(f"{section['type']} {i+1}:", styles['Heading4']))
        story.append(Paragraph(section['content'], code_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Full source code (abbreviated)
    story.append(Paragraph("LaTeX Source Code (First 2000 lines)", section_style))
    story.append(Spacer(1, 0.25*inch))
    
    # Show first 2000 characters of source
    preview = tex_content[:2000]
    if len(tex_content) > 2000:
        preview += "\n\n[... truncated ...]"
    
    story.append(Paragraph("Preview:", styles['Heading4']))
    story.append(Paragraph(preview, code_style))
    
    # Instructions
    story.append(PageBreak())
    story.append(Paragraph("How to Get Perfect PDF", section_style))
    story.append(Spacer(1, 0.25*inch))
    
    instructions = [
        "1. Open complete_derivations.html in a web browser",
        "2. Wait 10 seconds for MathJax to render equations",
        "3. Press Ctrl+P (or Cmd+P on Mac)",
        "4. Choose 'Save as PDF' as printer",
        "5. Adjust settings:",
        "   - Paper size: A4 or Letter",
        "   - Margins: Default",
        "   - Scale: 100%",
        "   - Check 'Background graphics'",
        "6. Save the PDF",
        "",
        "This will give you a perfect PDF with all equations rendered correctly."
    ]
    
    for line in instructions:
        story.append(Paragraph(line, normal_style))
    
    # Build PDF
    doc.build(story)
    return True

def main():
    if not HAS_REPORTLAB:
        print("Error: reportlab library not installed.")
        print("Install with: pip install reportlab")
        return 1
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    tex_file = Path("complete_derivations.tex")
    pdf_file = Path("complete_derivations_latex_source.pdf")
    
    if not tex_file.exists():
        print(f"Error: {tex_file} not found")
        return 1
    
    print(f"Creating PDF with LaTeX source code...")
    print(f"Source: {tex_file}")
    
    try:
        if create_latex_source_pdf(tex_file, pdf_file):
            size = pdf_file.stat().st_size / 1024
            print(f"✅ LaTeX source PDF created: {pdf_file} ({size:.1f} KB)")
            print(f"   This PDF shows the LaTeX source code.")
            print(f"   For rendered equations, use browser print-to-PDF on the HTML file.")
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