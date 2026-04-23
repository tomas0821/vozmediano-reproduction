#!/usr/bin/env python3
"""
Create an enhanced PDF with rendered equations using matplotlib.
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.lib import colors
    import matplotlib.pyplot as plt
    import matplotlib
    # Use non-interactive backend
    matplotlib.use('Agg')
    
    HAS_DEPS = True
except ImportError as e:
    print(f"Missing dependency: {e}")
    HAS_DEPS = False

def extract_equations_and_text(tex_file):
    """Extract equations and text from LaTeX file."""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove comments
    content = re.sub(r'%.*', '', content)
    
    # Extract document content between \begin{document} and \end{document}
    doc_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if doc_match:
        content = doc_match.group(1)
    
    # Split into sections
    sections = []
    
    # Find sections
    section_pattern = r'\\(section|subsection|subsubsection)\{([^}]+)\}'
    section_matches = list(re.finditer(section_pattern, content))
    
    for i, match in enumerate(section_matches):
        section_type = match.group(1)
        section_title = match.group(2)
        start_pos = match.end()
        
        # Find end of section (next section or end of document)
        if i + 1 < len(section_matches):
            end_pos = section_matches[i + 1].start()
        else:
            end_pos = len(content)
        
        section_content = content[start_pos:end_pos].strip()
        
        # Extract equations
        equations = []
        # Look for equation environments
        eq_envs = ['equation', 'align', 'eqnarray', 'gather']
        for env in eq_envs:
            pattern = r'\\begin\{' + env + r'\}(.*?)\\end\{' + env + r'\}'
            for eq_match in re.finditer(pattern, section_content, re.DOTALL):
                equations.append({
                    'latex': eq_match.group(1).strip(),
                    'env': env
                })
        
        # Also look for inline equations
        inline_pattern = r'\$(.*?)\$'
        for inline_match in re.finditer(inline_pattern, section_content):
            equations.append({
                'latex': inline_match.group(1).strip(),
                'env': 'inline'
            })
        
        # Remove equations from text for cleaner extraction
        text_content = section_content
        for eq in equations:
            if eq['env'] == 'inline':
                text_content = text_content.replace(f'${eq["latex"]}$', f'[EQUATION]')
            else:
                text_content = text_content.replace(f'\\begin{{{eq["env"]}}}{eq["latex"]}\\end{{{eq["env"]}}}', '[EQUATION]')
        
        # Clean up text
        text_content = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', text_content)  # Remove commands
        text_content = re.sub(r'\s+', ' ', text_content)  # Normalize whitespace
        text_content = text_content.strip()
        
        sections.append({
            'type': section_type,
            'title': section_title,
            'text': text_content,
            'equations': equations,
            'raw': section_content
        })
    
    return sections

def render_equation(latex_str, filename, dpi=150):
    """Render a LaTeX equation to an image."""
    try:
        plt.figure(figsize=(6, 1), dpi=dpi)
        plt.text(0.5, 0.5, f'${latex_str}$', fontsize=12, 
                ha='center', va='center')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(filename, bbox_inches='tight', pad_inches=0.1, dpi=dpi)
        plt.close()
        return True
    except Exception as e:
        print(f"  Warning: Could not render equation: {latex_str[:50]}...")
        print(f"  Error: {e}")
        return False

def create_enhanced_pdf(sections, pdf_file, temp_dir):
    """Create enhanced PDF with rendered equations."""
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
        fontSize=18,
        spaceAfter=24,
        textColor=colors.HexColor('#1a237e'),
        alignment=1  # Center
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.HexColor('#283593')
    )
    
    subsection_style = ParagraphStyle(
        'SubsectionStyle',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        textColor=colors.HexColor('#3949ab')
    )
    
    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        leading=14
    )
    
    equation_label_style = ParagraphStyle(
        'EquationLabel',
        parent=styles['Italic'],
        fontSize=10,
        spaceAfter=4,
        alignment=2  # Right
    )
    
    # Build story
    story = []
    
    # Title page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Complete Derivations for", title_style))
    story.append(Paragraph("Gauge fields and curvature in graphene", title_style))
    story.append(Paragraph("Vozmediano et al. (2008), arXiv:0807.3909", styles['Heading2']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Italic']))
    story.append(Paragraph("Enhanced PDF with rendered equations", styles['Italic']))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Contents", section_style))
    story.append(Spacer(1, 0.25*inch))
    
    for i, section in enumerate(sections):
        indent = ""
        if section['type'] == 'subsection':
            indent = "&nbsp;&nbsp;&nbsp;&nbsp;"
        elif section['type'] == 'subsubsection':
            indent = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        
        story.append(Paragraph(f"{indent}{i+1}. {section['title']}", normal_style))
    
    story.append(PageBreak())
    
    # Add sections
    for i, section in enumerate(sections):
        # Section title
        if section['type'] == 'section':
            story.append(Paragraph(f"{i+1}. {section['title']}", section_style))
        elif section['type'] == 'subsection':
            story.append(Paragraph(f"{i+1}. {section['title']}", subsection_style))
        else:
            story.append(Paragraph(section['title'], styles['Heading4']))
        
        # Section text
        if section['text']:
            # Replace [EQUATION] markers with actual equations
            text_parts = section['text'].split('[EQUATION]')
            eq_index = 0
            
            for part in text_parts:
                if part.strip():
                    story.append(Paragraph(part.strip(), normal_style))
                
                # Add equation if available
                if eq_index < len(section['equations']):
                    eq = section['equations'][eq_index]
                    if eq['env'] != 'inline':  # Skip inline for now
                        # Render equation
                        eq_filename = temp_dir / f"eq_{i}_{eq_index}.png"
                        if render_equation(eq['latex'], eq_filename):
                            img = Image(str(eq_filename), width=4*inch, height=0.5*inch)
                            story.append(img)
                            story.append(Spacer(1, 0.1*inch))
                    
                    eq_index += 1
        
        story.append(Spacer(1, 0.2*inch))
    
    # Add note
    story.append(PageBreak())
    story.append(Paragraph("Note", section_style))
    story.append(Paragraph("This is an enhanced PDF with rendered equations.", normal_style))
    story.append(Paragraph("For the complete document with perfect LaTeX formatting:", normal_style))
    story.append(Paragraph("1. View complete_derivations.html in a web browser", normal_style))
    story.append(Paragraph("2. Upload complete_derivations.tex to Overleaf.com", normal_style))
    story.append(Paragraph("3. Install LaTeX locally for full compilation", normal_style))
    
    # Build PDF
    doc.build(story)
    return True

def main():
    if not HAS_DEPS:
        print("Missing dependencies. Installing...")
        try:
            import subprocess
            subprocess.run([sys.executable, "-m", "pip", "install", "--user", 
                          "reportlab", "matplotlib"], check=True)
            print("Please run the script again.")
        except:
            print("Failed to install dependencies.")
            print("Install manually: pip install reportlab matplotlib")
        return 1
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    tex_file = Path("complete_derivations.tex")
    pdf_file = Path("complete_derivations_enhanced.pdf")
    
    if not tex_file.exists():
        print(f"Error: {tex_file} not found")
        return 1
    
    print(f"Creating enhanced PDF from LaTeX...")
    print(f"Source: {tex_file}")
    
    try:
        # Create temp directory for equation images
        temp_dir = Path("temp_eq_images")
        temp_dir.mkdir(exist_ok=True)
        
        # Extract content
        print("  Extracting equations and text...")
        sections = extract_equations_and_text(tex_file)
        print(f"  Found {len(sections)} sections")
        
        total_eqs = sum(len(s['equations']) for s in sections)
        print(f"  Found {total_eqs} equations")
        
        # Create PDF
        print("  Creating enhanced PDF...")
        if create_enhanced_pdf(sections, pdf_file, temp_dir):
            # Clean up temp files
            for file in temp_dir.glob("*.png"):
                file.unlink()
            temp_dir.rmdir()
            
            size = pdf_file.stat().st_size / 1024
            print(f"✅ Enhanced PDF created: {pdf_file} ({size:.1f} KB)")
            print(f"   Contains rendered equations and section structure.")
            print(f"   For perfect LaTeX: use Overleaf.com")
            return 0
        else:
            print("✗ Failed to create enhanced PDF")
            return 1
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())