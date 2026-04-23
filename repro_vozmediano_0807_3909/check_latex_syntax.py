#!/usr/bin/env python3
"""
Basic LaTeX syntax checker.
Checks for common issues like unmatched braces, missing \end, etc.
"""

import re
import sys
from pathlib import Path

def check_latex_syntax(filepath):
    """Check LaTeX file for common syntax issues."""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check 1: Unmatched braces
    brace_stack = []
    for i, char in enumerate(content):
        if char == '{':
            brace_stack.append(i)
        elif char == '}':
            if brace_stack:
                brace_stack.pop()
            else:
                issues.append(f"Unmatched '}}' at position {i}")
    
    if brace_stack:
        for pos in brace_stack:
            issues.append(f"Unmatched '{{' at position {pos}")
    
    # Check 2: \begin without \end and vice versa
    begins = list(re.finditer(r'\\begin\{([^}]+)\}', content))
    ends = list(re.finditer(r'\\end\{([^}]+)\}', content))
    
    begin_envs = [(m.group(1), m.start()) for m in begins]
    end_envs = [(m.group(1), m.start()) for m in ends]
    
    # Simple check: count should match
    if len(begin_envs) != len(end_envs):
        issues.append(f"Mismatched begin/end: {len(begin_envs)} \\begin vs {len(end_envs)} \\end")
    
    # Check 3: Missing document class
    if not re.search(r'\\documentclass', content):
        issues.append("Missing \\documentclass")
    
    # Check 4: Missing \begin{document} or \end{document}
    if not re.search(r'\\begin\{document\}', content):
        issues.append("Missing \\begin{document}")
    if not re.search(r'\\end\{document\}', content):
        issues.append("Missing \\end{document}")
    
    # Check 5: Common commands that might need packages
    package_commands = {
        r'\\mathbb': 'amsfonts or amssymb',
        r'\\mathcal': 'amsfonts',
        r'\\mathbf': 'amsmath',
        r'\\boldsymbol': 'amsmath',
        r'\\mathscr': 'mathrsfs',
        r'\\mathfrak': 'amssymb',
        r'\\DeclareMathOperator': 'amsmath',
        r'\\renewcommand': 'usually needs specific package',
    }
    
    for cmd, package in package_commands.items():
        if re.search(cmd, content):
            # Check if corresponding package is included
            if package not in ['usually needs specific package']:
                pkg_pattern = r'\\usepackage.*\{.*' + re.escape(package) + r'.*\}'
                if not re.search(pkg_pattern, content, re.IGNORECASE):
                    issues.append(f"Command {cmd} might need package '{package}'")
    
    return issues

def main():
    tex_file = Path("complete_derivations.tex")
    
    if not tex_file.exists():
        print(f"Error: {tex_file} not found")
        return 1
    
    print(f"Checking LaTeX syntax: {tex_file}")
    print(f"File size: {tex_file.stat().st_size / 1024:.1f} KB")
    print()
    
    issues = check_latex_syntax(tex_file)
    
    if not issues:
        print("✅ No major syntax issues found")
        print("The LaTeX file appears to be syntactically valid.")
        return 0
    
    print(f"⚠️  Found {len(issues)} potential issue(s):")
    for i, issue in enumerate(issues, 1):
        print(f"  {i}. {issue}")
    
    print()
    print("Note: These are basic checks. Full compilation is needed to verify.")
    return 0

if __name__ == "__main__":
    sys.exit(main())