# LaTeX Compilation Guide

This guide provides multiple methods to compile the LaTeX document `complete_derivations.tex`.

## Current Status

✅ **HTML version already created**: `complete_derivations.html`
- Contains all content with MathJax for equations
- Can be viewed in any web browser
- File size: 34.0 KB

## Available Compilation Methods

### Method 1: View HTML (Easiest, Already Done)
```bash
# Open in default browser
xdg-open complete_derivations.html

# Or with specific browser
firefox complete_derivations.html
chrome complete_derivations.html
```

### Method 2: Local LaTeX Installation (Recommended for PDF)

#### Option A: Install system-wide (requires sudo)
```bash
sudo dnf install texlive texlive-amsmath texlive-amssymb texlive-amsthm \
    texlive-graphics texlive-hyperref texlive-geometry texlive-booktabs \
    texlive-physics texlive-siunitx texlive-latexmk
```

Then compile:
```bash
# Run the compilation script
./compile_latex.sh

# Or manually
pdflatex complete_derivations.tex
pdflatex complete_derivations.tex  # Run twice for references
pdflatex complete_derivations.tex  # Run third time for final
```

#### Option B: User-space installation (if available)
Check if your system has a user-space package manager like `conda`:
```bash
conda install -c conda-forge texlive-core
```

### Method 3: Docker (No Local Installation Needed)

**Prerequisite**: Docker must be installed and running.

```bash
# Make script executable
chmod +x compile_with_docker.sh

# Run compilation
./compile_with_docker.sh
```

This will:
1. Download the texlive Docker image (≈2GB on first run)
2. Compile the LaTeX document inside a container
3. Output `complete_derivations.pdf`

### Method 4: Online LaTeX Editors

#### Overleaf (Free Online)
1. Go to [overleaf.com](https://www.overleaf.com)
2. Create a new project
3. Upload `complete_derivations.tex`
4. Click "Recompile"

#### ShareLaTeX
Similar to Overleaf (they merged, but both work)

### Method 5: Recreate HTML (if needed)
```bash
# Install pandoc if not available
sudo dnf install pandoc

# Convert LaTeX to HTML
pandoc complete_derivations.tex -o complete_derivations.html --mathjax --standalone
```

## File Descriptions

### Generated Files
- `complete_derivations.html` - HTML version with MathJax (already exists)
- `complete_derivations.pdf` - PDF version (will be created if LaTeX compiles)

### Scripts
- `compile_latex.sh` - Local LaTeX compilation script
- `compile_with_docker.sh` - Docker-based compilation
- `compile_latex.py` - Python script with multiple fallback methods

## Package Requirements

The LaTeX document requires these packages:
- `amsmath`, `amssymb`, `amsthm` - Mathematical symbols and theorems
- `graphicx` - Graphics inclusion
- `hyperref` - Hyperlinks in PDF
- `geometry` - Page layout
- `booktabs` - Professional tables
- `physics` - Physics notation
- `siunitx` - SI units

## Troubleshooting

### "Command not found: pdflatex"
- Install LaTeX using Method 2
- Use Docker (Method 3)
- Use online editor (Method 4)

### Docker errors
- Ensure Docker is installed: `docker --version`
- Ensure Docker daemon is running: `sudo systemctl start docker`
- Check permissions: `sudo usermod -aG docker $USER` (log out and back in)

### Missing LaTeX packages
If compilation fails with missing package errors:
```bash
# Search for package
dnf search texlive-<package-name>

# Install missing package
sudo dnf install texlive-<package-name>
```

### Math equations not rendering in HTML
- HTML uses MathJax CDN (requires internet connection)
- For offline use, download MathJax locally or use PDF

## Quick Start

For immediate viewing:
```bash
# Open HTML in browser
firefox complete_derivations.html
```

For PDF creation (if you have LaTeX or Docker):
```bash
# Try Python script with multiple methods
python3 compile_latex.py
```

## Recommendations

1. **Quick viewing**: Use the existing HTML file
2. **PDF for sharing/printing**: Install LaTeX locally or use Docker
3. **Collaboration**: Use Overleaf for online editing and compilation
4. **Minimal setup**: HTML + MathJax works well for most purposes

The HTML version preserves all mathematical content via MathJax and is immediately viewable without any installation.