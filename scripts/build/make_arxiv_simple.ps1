# CTMCK arXiv Package Builder (PowerShell)
Write-Host "Building CTMCK arXiv submission package..." -ForegroundColor Green

# Define paths
$RootDir = Get-Location
$SourceDir = "$RootDir\..\ctmck_v03_package\ctmck_v03_source"
$BuildDir = "$RootDir\build"
$ArxivDir = "$BuildDir\arxiv_pkg"

# Clean and create build directory
Write-Host "Setting up build directory..." -ForegroundColor Yellow
if (Test-Path $BuildDir) { Remove-Item $BuildDir -Recurse -Force }
New-Item -ItemType Directory -Path "$ArxivDir\figures" -Force | Out-Null
New-Item -ItemType Directory -Path "$ArxivDir\sections" -Force | Out-Null

# Copy main LaTeX file
Write-Host "Copying main LaTeX source..." -ForegroundColor Yellow
Copy-Item "docs\ctmck_article_v03.tex" "$ArxivDir\"

# Copy section files
Write-Host "Copying section files..." -ForegroundColor Yellow
if (Test-Path "$SourceDir\sections") {
    Copy-Item "$SourceDir\sections\*.tex" "$ArxivDir\sections\"
} else {
    Write-Host "Warning: sections directory not found" -ForegroundColor Orange
}

# Copy bibliography
Write-Host "Copying bibliography..." -ForegroundColor Yellow
if (Test-Path "$SourceDir\references.bib") {
    Copy-Item "$SourceDir\references.bib" "$ArxivDir\"
} elseif (Test-Path "references.bib") {
    Copy-Item "references.bib" "$ArxivDir\"
} else {
    Write-Host "Warning: references.bib not found" -ForegroundColor Orange
}

# Copy figures
Write-Host "Copying figures..." -ForegroundColor Yellow
if (Test-Path "figures\*.png") {
    Copy-Item "figures\*.png" "$ArxivDir\figures\"
} else {
    Write-Host "Warning: No PNG figures found" -ForegroundColor Orange
}

# Create ZIP package
Write-Host "Creating ZIP package..." -ForegroundColor Yellow
Push-Location $BuildDir
Compress-Archive -Path "arxiv_pkg" -DestinationPath "ctmck_v03_arxiv.zip" -Force
Pop-Location

# Display results
Write-Host ""
Write-Host "arXiv package created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Package contents:" -ForegroundColor Cyan
Get-ChildItem $ArxivDir -Recurse -File | ForEach-Object { 
    $relativePath = $_.FullName.Replace("$ArxivDir\", "")
    Write-Host "  $relativePath" -ForegroundColor White
}
Write-Host ""
Write-Host "Output package: $BuildDir\ctmck_v03_arxiv.zip" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ready for arXiv submission!" -ForegroundColor Green
