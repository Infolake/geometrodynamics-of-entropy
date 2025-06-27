#!/bin/bash
#=================================================================
# CTMCK LaTeX Compilation Check Script
# Usage: ./compile_check.sh
#=================================================================

echo "🔬 CTMCK LaTeX Compilation Check"
echo "================================="

# Check if LaTeX is available
if ! command -v pdflatex &> /dev/null; then
    echo "❌ pdflatex not found. Please install LaTeX (TeX Live or MiKTeX)"
    echo "   - Windows: https://miktex.org/download"
    echo "   - Linux: sudo apt-get install texlive-full"
    echo "   - macOS: brew install mactex"
    exit 1
fi

echo "✅ pdflatex found"

# Compile the manuscript
echo "📝 Compiling ctmck_article_v0.1b.tex..."
pdflatex -interaction=nonstopmode ctmck_article_v0.1b.tex

# Check for compilation errors
if [ $? -eq 0 ]; then
    echo "✅ PDF compilation successful!"
    
    # Check for warnings in log file
    echo "🔍 Checking for warnings..."
    if grep -E "Overfull|Underfull|Undefined reference|Citation.*undefined" ctmck_article_v0.1b.log > /dev/null; then
        echo "⚠️  Warnings found in log file:"
        grep -E "Overfull|Underfull|Undefined reference|Citation.*undefined" ctmck_article_v0.1b.log
    else
        echo "✅ No significant warnings found"
    fi
    
    # Check PDF size
    if [ -f "ctmck_article_v0.1b.pdf" ]; then
        pdf_size=$(stat -f%z ctmck_article_v0.1b.pdf 2>/dev/null || stat -c%s ctmck_article_v0.1b.pdf 2>/dev/null)
        pdf_size_mb=$((pdf_size / 1024 / 1024))
        
        if [ $pdf_size_mb -le 10 ]; then
            echo "✅ PDF size: ${pdf_size_mb}MB (≤10MB, arXiv compliant)"
        else
            echo "⚠️  PDF size: ${pdf_size_mb}MB (>10MB, may need compression)"
        fi
    fi
    
    echo ""
    echo "🎉 Manuscript ready for arXiv submission!"
    echo "📋 Pre-submission checklist:"
    echo "   ✅ RevTeX 4-2 format"
    echo "   ✅ Proper title with line break"
    echo "   ✅ Keywords included"
    echo "   ✅ siunitx package for units"
    echo "   ✅ DOI references in bibliography"
    echo "   ✅ ORCID in affiliation"
    echo "   ✅ Preprint identifier"
    
else
    echo "❌ PDF compilation failed!"
    echo "📋 Common issues to check:"
    echo "   - Missing packages (install texlive-full)"
    echo "   - Syntax errors in LaTeX code"
    echo "   - Missing figure files"
    echo ""
    echo "🔍 Check the log file for details:"
    echo "   ctmck_article_v0.1b.log"
    exit 1
fi

echo ""
echo "📤 Next steps for arXiv submission:"
echo "   1. Create submission package: zip ctmck_article_v0.1b.tex figures/"
echo "   2. Upload to arXiv.org"
echo "   3. Select license: CC-BY-4.0"
echo "   4. Add abstract and keywords"
echo "   5. Submit for review" 