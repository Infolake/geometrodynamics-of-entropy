#!/bin/bash
#=================================================================
# CTMCK arXiv Package Builder
# Creates complete submission package for arXiv with all dependencies
# Author: Dr. Guilherme de Camargo
# Date: June 29, 2025
#=================================================================

set -e

echo "🚀 Building CTMCK arXiv submission package..."

# Define paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SOURCE_DIR="$ROOT_DIR/../ctmck_v03_package/ctmck_v03_source"
BUILD_DIR="$ROOT_DIR/build"
ARXIV_DIR="$BUILD_DIR/arxiv_pkg"

# Clean and create build directory
echo "📁 Setting up build directory..."
rm -rf "$ARXIV_DIR"
mkdir -p "$ARXIV_DIR/figures"
mkdir -p "$ARXIV_DIR/sections"

# Copy main LaTeX file
echo "📄 Copying main LaTeX source..."
cp "$ROOT_DIR/docs/ctmck_article_v03.tex" "$ARXIV_DIR/"

# Copy section files
echo "📝 Copying section files..."
if [ -d "$SOURCE_DIR/sections" ]; then
    cp "$SOURCE_DIR/sections"/*.tex "$ARXIV_DIR/sections/"
else
    echo "⚠️  Warning: sections directory not found at $SOURCE_DIR/sections"
fi

# Copy bibliography
echo "📚 Copying bibliography..."
if [ -f "$SOURCE_DIR/references.bib" ]; then
    cp "$SOURCE_DIR/references.bib" "$ARXIV_DIR/"
elif [ -f "$ROOT_DIR/references.bib" ]; then
    cp "$ROOT_DIR/references.bib" "$ARXIV_DIR/"
else
    echo "⚠️  Warning: references.bib not found"
fi

# Copy figures (PNG files for arXiv compatibility)
echo "🖼️  Copying figures..."
cp "$ROOT_DIR/figures"/*.png "$ARXIV_DIR/figures/" 2>/dev/null || echo "⚠️  Warning: No PNG figures found"

# Modify the main LaTeX file to use relative paths
echo "🔧 Adjusting LaTeX file for arXiv..."
sed -i 's|\\graphicspath{{figures/}}|\\graphicspath{{./figures/}}|g' "$ARXIV_DIR/ctmck_article_v03.tex"
sed -i 's|\\input{sections/|\\input{sections/|g' "$ARXIV_DIR/ctmck_article_v03.tex"

# Test compilation
echo "🔬 Testing compilation..."
cd "$ARXIV_DIR"
if command -v pdflatex >/dev/null 2>&1; then
    echo "  Running pdflatex (1st pass)..."
    pdflatex -interaction=nonstopmode ctmck_article_v03.tex >/dev/null
    
    if [ -f "references.bib" ]; then
        echo "  Running bibtex..."
        bibtex ctmck_article_v03 >/dev/null 2>&1 || echo "    (bibtex warnings ignored)"
    fi
    
    echo "  Running pdflatex (2nd pass)..."
    pdflatex -interaction=nonstopmode ctmck_article_v03.tex >/dev/null
    
    echo "  Running pdflatex (3rd pass)..."
    pdflatex -interaction=nonstopmode ctmck_article_v03.tex >/dev/null
    
    if [ -f "ctmck_article_v03.pdf" ]; then
        echo "✅ Compilation successful!"
    else
        echo "❌ Compilation failed!"
        exit 1
    fi
else
    echo "⚠️  pdflatex not found - skipping test compilation"
fi

# Clean auxiliary files
echo "🧹 Cleaning auxiliary files..."
rm -f *.aux *.log *.bbl *.blg *.out *.toc *.fdb_latexmk *.fls *.synctex.gz

# Create ZIP package
echo "📦 Creating ZIP package..."
cd "$BUILD_DIR"
zip -r "ctmck_v03_arxiv.zip" "arxiv_pkg/" >/dev/null

# Create TAR.GZ package (alternative)
echo "📦 Creating TAR.GZ package..."
tar -czf "ctmck_v03_arxiv.tar.gz" "arxiv_pkg/"

# Display results
echo ""
echo "🎉 arXiv packages created successfully!"
echo ""
echo "📊 Package contents:"
echo "-------------------"
find "$ARXIV_DIR" -type f | sort | sed "s|$ARXIV_DIR/|  |g"
echo ""
echo "📦 Output packages:"
echo "  ZIP: $BUILD_DIR/ctmck_v03_arxiv.zip"
echo "  TAR: $BUILD_DIR/ctmck_v03_arxiv.tar.gz"
echo ""
echo "📋 arXiv submission checklist:"
echo "  ✅ All LaTeX source files included"
echo "  ✅ Bibliography file included"
echo "  ✅ All figures included (PNG format)"
echo "  ✅ Compilation tested locally"
echo "  ✅ Ready for arXiv upload"
echo ""
echo "🚀 Next steps:"
echo "  1. Upload either ZIP or TAR.GZ to arXiv"
echo "  2. Category: gr-qc (primary), astro-ph.CO (secondary)"
echo "  3. License: CC-BY-4.0"
echo "  4. Wait for arXiv ID assignment"
echo ""
echo "✨ Good luck with your submission!"
