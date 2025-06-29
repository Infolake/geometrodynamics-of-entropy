#!/bin/bash

# =======================================================
#  CTMCK LaTeX Compilation & Quality Check Script
# =======================================================

set -e  # Exit on any error

echo "=============================================="
echo "  CTMCK Article Compilation & Quality Check"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "docs/ctmck_article_v03.tex" ]; then
    echo -e "${RED}ERROR: ctmck_article_v03.tex not found in docs/ directory${NC}"
    echo "Please run this script from the repository root."
    exit 1
fi

# Create temporary build directory
BUILD_DIR="build_temp"
mkdir -p "$BUILD_DIR"

echo -e "${YELLOW}[1/4] Copying files to build directory...${NC}"
cp docs/ctmck_article_v03.tex "$BUILD_DIR/"
cp -r figures "$BUILD_DIR/"
cp references.bib "$BUILD_DIR/" 2>/dev/null || echo "Warning: references.bib not found"

cd "$BUILD_DIR"

echo -e "${YELLOW}[2/4] First LaTeX compilation pass...${NC}"
if ! pdflatex -interaction=nonstopmode ctmck_article_v03.tex > compile1.log 2>&1; then
    echo -e "${RED}ERROR: First compilation pass failed${NC}"
    echo "Check compile1.log for details:"
    tail -20 compile1.log
    exit 1
fi

echo -e "${YELLOW}[3/4] Second LaTeX compilation pass (resolving references)...${NC}"
if ! pdflatex -interaction=nonstopmode ctmck_article_v03.tex > compile2.log 2>&1; then
    echo -e "${RED}ERROR: Second compilation pass failed${NC}"
    echo "Check compile2.log for details:"
    tail -20 compile2.log
    exit 1
fi

echo -e "${YELLOW}[4/4] Quality checks...${NC}"

# Check for common LaTeX warnings
WARNINGS=$(grep -i "warning\|undefined\|multiply defined\|overfull\|underfull" *.log | wc -l)
if [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}Found $WARNINGS potential issues:${NC}"
    grep -i "warning\|undefined\|multiply defined" *.log | head -10
fi

# Check PDF was generated
if [ ! -f "ctmck_article_v03.pdf" ]; then
    echo -e "${RED}ERROR: PDF was not generated${NC}"
    exit 1
fi

# Check PDF file size (should be > 500KB for a paper with figures)
PDF_SIZE=$(wc -c < ctmck_article_v03.pdf)
if [ "$PDF_SIZE" -lt 500000 ]; then
    echo -e "${YELLOW}Warning: PDF size is only ${PDF_SIZE} bytes (expected > 500KB)${NC}"
fi

# Copy final PDF back
cp ctmck_article_v03.pdf ../docs/

cd ..
rm -rf "$BUILD_DIR"

echo -e "${GREEN}=============================================="
echo -e "  Compilation completed successfully!"
echo -e "  Generated: docs/ctmck_article_v03.pdf"
echo -e "  Size: $(ls -lh docs/ctmck_article_v03.pdf | awk '{print $5}')"
echo -e "=============================================${NC}"

echo
echo "Quality check summary:"
echo "- LaTeX warnings: $WARNINGS"
echo "- PDF generated: ✓"
echo "- File size check: $([ "$PDF_SIZE" -gt 500000 ] && echo "✓" || echo "⚠")"

if command -v pdfinfo &> /dev/null; then
    echo "- Page count: $(pdfinfo docs/ctmck_article_v03.pdf 2>/dev/null | grep Pages | awk '{print $2}')"
fi

echo
echo "Next steps:"
echo "1. Review docs/ctmck_article_v03.pdf"
echo "2. If satisfied, tag release: git tag v0.3_draft"
echo "3. Create Zenodo release with this PDF"
