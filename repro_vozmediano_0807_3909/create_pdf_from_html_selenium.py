#!/usr/bin/env python3
"""
Create PDF from HTML using Selenium to capture MathJax-rendered equations.
"""

import sys
import os
import time
from pathlib import Path
import tempfile
import base64

def check_selenium():
    """Check if Selenium is available."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        return True
    except ImportError:
        return False

def install_selenium():
    """Install Selenium and dependencies."""
    print("Installing Selenium and dependencies...")
    try:
        import subprocess
        subprocess.run([
            sys.executable, "-m", "pip", "install", "--user",
            "selenium", "webdriver-manager", "pillow"
        ], check=True)
        print("Installation successful. Please run the script again.")
        return True
    except Exception as e:
        print(f"Installation failed: {e}")
        return False

def create_pdf_with_selenium(html_file, pdf_file):
    """Create PDF using Selenium and Chrome."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        print("Setting up Chrome for PDF generation...")
        
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Enable printing
        chrome_options.add_argument("--disable-software-rasterizer")
        
        # Try to use existing Chrome if available
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except:
            # Try with webdriver-manager
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Get absolute path to HTML file
        abs_html_path = Path(html_file).resolve()
        file_url = f"file://{abs_html_path}"
        
        print(f"Loading HTML: {file_url}")
        driver.get(file_url)
        
        # Wait for MathJax to render (increase wait time for complex equations)
        print("Waiting for MathJax to render equations...")
        time.sleep(10)  # Give MathJax plenty of time
        
        # Check if MathJax is loaded
        try:
            mathjax_status = driver.execute_script("return typeof MathJax !== 'undefined'")
            if mathjax_status:
                print("MathJax detected, waiting for rendering...")
                # Wait for MathJax to finish
                driver.execute_script("""
                    if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
                        return MathJax.typesetPromise();
                    }
                    return Promise.resolve();
                """)
                time.sleep(5)
        except:
            print("Could not check MathJax status, continuing...")
        
        # Print to PDF
        print("Generating PDF...")
        
        # Use Chrome's print-to-PDF
        print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True,
            'paperWidth': 8.5,  # Letter width in inches
            'paperHeight': 11,   # Letter height in inches
            'marginTop': 0.5,
            'marginBottom': 0.5,
            'marginLeft': 0.5,
            'marginRight': 0.5,
        }
        
        result = driver.execute_cdp_cmd("Page.printToPDF", print_options)
        pdf_data = base64.b64decode(result['data'])
        
        with open(pdf_file, 'wb') as f:
            f.write(pdf_data)
        
        driver.quit()
        return True
        
    except Exception as e:
        print(f"Error with Selenium: {e}")
        import traceback
        traceback.print_exc()
        return False

def create_pdf_with_weasyprint(html_file, pdf_file):
    """Fallback: Use WeasyPrint if available."""
    try:
        from weasyprint import HTML
        print("Trying WeasyPrint...")
        HTML(html_file).write_pdf(pdf_file)
        return True
    except ImportError:
        print("WeasyPrint not installed")
        return False
    except Exception as e:
        print(f"WeasyPrint error: {e}")
        return False

def main():
    # Check dependencies
    if not check_selenium():
        print("Selenium not available.")
        response = input("Install Selenium and Chrome WebDriver? (y/n): ")
        if response.lower() == 'y':
            if install_selenium():
                return 0
            else:
                print("Installation failed. Trying alternative methods...")
        else:
            print("Trying alternative methods...")
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    html_file = Path("complete_derivations.html")
    pdf_file = Path("complete_derivations_mathjax.pdf")
    
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        print("First generate HTML with: python3 compile_latex.py")
        return 1
    
    print(f"=== Creating PDF from MathJax-rendered HTML ===")
    print(f"Source: {html_file}")
    print(f"Target: {pdf_file}")
    print()
    
    # Try Selenium first (best quality)
    print("Method 1: Selenium + Chrome (best for MathJax)")
    if check_selenium():
        if create_pdf_with_selenium(html_file, pdf_file):
            if pdf_file.exists():
                size = pdf_file.stat().st_size / 1024
                print(f"✅ PDF created with MathJax equations: {pdf_file} ({size:.1f} KB)")
                print("   Equations should be properly rendered.")
                return 0
    else:
        print("  Selenium not available")
    
    print()
    print("Method 2: WeasyPrint (fallback)")
    if create_pdf_with_weasyprint(html_file, pdf_file):
        if pdf_file.exists():
            size = pdf_file.stat().st_size / 1024
            print(f"✅ PDF created with WeasyPrint: {pdf_file} ({size:.1f} KB)")
            print("   Note: MathJax equations may not render perfectly.")
            return 0
    
    print()
    print("❌ All automated methods failed.")
    print()
    print("=== MANUAL SOLUTION (Recommended) ===")
    print("Since automated PDF generation is challenging with MathJax,")
    print("here's the best manual approach:")
    print()
    print("1. Open the HTML file in Chrome/Firefox:")
    print(f"   firefox {html_file}")
    print()
    print("2. Wait for equations to render (5-10 seconds)")
    print()
    print("3. Print to PDF:")
    print("   - Press Ctrl+P (or Cmd+P on Mac)")
    print("   - Choose 'Save as PDF' as printer")
    print("   - Adjust settings if needed:")
    print("     * Paper size: Letter or A4")
    print("     * Margins: Default or None")
    print("     * Scale: 100%")
    print("   - Click 'Save'")
    print()
    print("This will give you a perfect PDF with all equations rendered.")
    
    return 1

if __name__ == "__main__":
    sys.exit(main())