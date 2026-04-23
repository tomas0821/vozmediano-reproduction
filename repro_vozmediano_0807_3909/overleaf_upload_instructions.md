# Upload to Overleaf for Online Compilation

Overleaf is a free online LaTeX editor that can compile your document without any local installation.

## Method 1: Manual Upload (Easiest)

1. Go to [overleaf.com](https://www.overleaf.com)
2. Create a free account or log in
3. Click "New Project" → "Upload Project"
4. Select `complete_derivations.tex` from your computer
5. Click "Open" to upload
6. Overleaf will automatically compile the document
7. Download the PDF from the "Download PDF" button

## Method 2: Create Project from ZIP

If you have multiple files:
```bash
# Create a ZIP of the LaTeX file (and any supporting files)
zip vozmediano_derivations.zip complete_derivations.tex

# Upload the ZIP to Overleaf
```

## Method 3: Using Overleaf API (Advanced)

If you have an Overleaf account with API access:

```bash
# Install overleaf-cli if available
# pip install overleaf-cli

# Upload project
overleaf upload complete_derivations.tex --project-name "Vozmediano Derivations"
```

## Required Packages in Overleaf

Overleaf includes most LaTeX packages by default. If you get compilation errors about missing packages:

1. Click "Recompile" to see the error log
2. Add missing packages to the preamble:
```latex
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{booktabs}
\usepackage{physics}
\usepackage{siunitx}
```

These packages are already included in `complete_derivations.tex`.

## Benefits of Overleaf

- **No installation required** - works in browser
- **Real-time compilation** - see errors immediately
- **Collaboration** - share with others
- **Version history** - track changes
- **Templates** - many LaTeX templates available

## Quick Start Link

You can use this direct link to create a new project:
[https://www.overleaf.com/project/new](https://www.overleaf.com/project/new)

Then drag and drop `complete_derivations.tex` into the file list.

## Troubleshooting Overleaf

### "Undefined control sequence"
- Check if package is included in preamble
- Overleaf might use different package names

### "File not found" for included files
- Upload all referenced files (.bib, .sty, images, etc.)
- Use relative paths

### Compilation timeout
- Large documents may time out on free tier
- Try breaking into smaller files
- Or compile sections separately

## Alternative Online Editors

1. **ShareLaTeX** - Similar to Overleaf (they merged)
2. **Papeeria** - Another online LaTeX editor
3. **Authorea** - Collaborative scientific writing

## Recommendation

For one-time compilation of `complete_derivations.tex`, **Method 1 (manual upload)** is simplest and requires no technical setup.