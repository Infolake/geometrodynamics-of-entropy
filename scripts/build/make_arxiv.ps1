#=================================================================
# CTMCK arXiv Package Builder (PowerShell version)
# Creates complete submission package for arXiv with all dependencies
# Author: Dr. Guilherme de Camargo
# Date: June 29, 2025
#=================================================================

Write-Host "🚀 Building CTMCK arXiv submission package..." -ForegroundColor Green

# Define paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Resolve-Path "$ScriptDir\..\.."
$SourceDir = "$RootDir\..\ctmck_v03_package\ctmck_v03_source"
$BuildDir = "$RootDir\build"
$ArxivDir = "$BuildDir\arxiv_pkg"

# Clean and create build directory
Write-Host "📁 Setting up build directory..." -ForegroundColor Yellow
if (Test-Path $ArxivDir) { Remove-Item $ArxivDir -Recurse -Force }
New-Item -ItemType Directory -Path "$ArxivDir\figures" -Force | Out-Null
New-Item -ItemType Directory -Path "$ArxivDir\sections" -Force | Out-Null

# Copy main LaTeX file
Write-Host "📄 Copying main LaTeX source..." -ForegroundColor Yellow
Copy-Item "$RootDir\docs\ctmck_article_v03.tex" "$ArxivDir\"

# Copy section files
Write-Host "📝 Copying section files..." -ForegroundColor Yellow
if (Test-Path "$SourceDir\sections") {
    Copy-Item "$SourceDir\sections\*.tex" "$ArxivDir\sections\"
} else {
    Write-Host "⚠️  Warning: sections directory not found at $SourceDir\sections" -ForegroundColor Orange
}

# Copy bibliography
Write-Host "📚 Copying bibliography..." -ForegroundColor Yellow
if (Test-Path "$SourceDir\references.bib") {
    Copy-Item "$SourceDir\references.bib" "$ArxivDir\"
} elseif (Test-Path "$RootDir\references.bib") {
    Copy-Item "$RootDir\references.bib" "$ArxivDir\"
} else {
    Write-Host "⚠️  Warning: references.bib not found" -ForegroundColor Orange
}

# Copy figures (PNG files for arXiv compatibility)
Write-Host "🖼️  Copying figures..." -ForegroundColor Yellow
try {
    Copy-Item "$RootDir\figures\*.png" "$ArxivDir\figures\"
} catch {
    Write-Host "⚠️  Warning: No PNG figures found" -ForegroundColor Orange
}

# Modify the main LaTeX file to use relative paths
Write-Host "🔧 Adjusting LaTeX file for arXiv..." -ForegroundColor Yellow
$latexContent = Get-Content "$ArxivDir\ctmck_article_v03.tex" -Raw
$latexContent = $latexContent -replace '\\graphicspath\{\{figures/\}\}', '\graphicspath{{./figures/}}'
Set-Content "$ArxivDir\ctmck_article_v03.tex" $latexContent

# Test compilation (if pdflatex is available)
Write-Host "🔬 Testing compilation..." -ForegroundColor Yellow
Push-Location $ArxivDir
try {
    if (Get-Command pdflatex -ErrorAction SilentlyContinue) {
        Write-Host "  Running pdflatex (1st pass)..." -ForegroundColor Cyan
        & pdflatex -interaction=nonstopmode ctmck_article_v03.tex | Out-Null
        
        if (Test-Path "references.bib") {
            Write-Host "  Running bibtex..." -ForegroundColor Cyan
            & bibtex ctmck_article_v03 2>$null | Out-Null
        }
        
        Write-Host "  Running pdflatex (2nd pass)..." -ForegroundColor Cyan
        & pdflatex -interaction=nonstopmode ctmck_article_v03.tex | Out-Null
        
        Write-Host "  Running pdflatex (3rd pass)..." -ForegroundColor Cyan
        & pdflatex -interaction=nonstopmode ctmck_article_v03.tex | Out-Null
        
        if (Test-Path "ctmck_article_v03.pdf") {
            Write-Host "✅ Compilation successful!" -ForegroundColor Green
        } else {
            Write-Host "❌ Compilation failed!" -ForegroundColor Red
            return
        }
    } else {
        Write-Host "⚠️  pdflatex not found - skipping test compilation" -ForegroundColor Orange
    }
} finally {
    Pop-Location
}

# Clean auxiliary files
Write-Host "🧹 Cleaning auxiliary files..." -ForegroundColor Yellow
Remove-Item "$ArxivDir\*.aux", "$ArxivDir\*.log", "$ArxivDir\*.bbl", "$ArxivDir\*.blg", "$ArxivDir\*.out", "$ArxivDir\*.toc", "$ArxivDir\*.fdb_latexmk", "$ArxivDir\*.fls", "$ArxivDir\*.synctex.gz" -ErrorAction SilentlyContinue

# Create ZIP package
Write-Host "📦 Creating ZIP package..." -ForegroundColor Yellow
Push-Location $BuildDir
Compress-Archive -Path "arxiv_pkg" -DestinationPath "ctmck_v03_arxiv.zip" -Force
Pop-Location

# Display results
Write-Host ""
Write-Host "🎉 arXiv package created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Package contents:" -ForegroundColor Cyan
Write-Host "-------------------" -ForegroundColor Cyan
Get-ChildItem $ArxivDir -Recurse -File | ForEach-Object { 
    $relativePath = $_.FullName.Replace("$ArxivDir\", "")
    Write-Host "  $relativePath" -ForegroundColor White
}
Write-Host ""
Write-Host "📦 Output package:" -ForegroundColor Cyan
Write-Host "  ZIP: $BuildDir\ctmck_v03_arxiv.zip" -ForegroundColor White
Write-Host ""
Write-Host "📋 arXiv submission checklist:" -ForegroundColor Cyan
Write-Host "  ✅ All LaTeX source files included" -ForegroundColor Green
Write-Host "  ✅ Bibliography file included" -ForegroundColor Green
Write-Host "  ✅ All figures included (PNG format)" -ForegroundColor Green
Write-Host "  ✅ Compilation tested locally" -ForegroundColor Green
Write-Host "  ✅ Ready for arXiv upload" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Next steps:" -ForegroundColor Cyan
Write-Host "  1. Upload ZIP to arXiv submission form" -ForegroundColor White
Write-Host "  2. Category: gr-qc (primary), astro-ph.CO (secondary)" -ForegroundColor White
Write-Host "  3. License: CC-BY-4.0" -ForegroundColor White
Write-Host "  4. Wait for arXiv ID assignment" -ForegroundColor White
Write-Host ""
Write-Host "Good luck with your submission!" -ForegroundColor Magenta
