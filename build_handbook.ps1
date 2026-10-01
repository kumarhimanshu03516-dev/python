<#
.SYNOPSIS
Build the Python Handbook PDF and copy it to E:\pdf\python_handbook.pdf

.REQUIREMENTS
- MiKTeX (or TeX Live) installed and on PATH (xelatex, latexmk)
- Python 3.9+ installed
#>

# ---------------------------------------------------------
# Config – change only if your layout differs
# ---------------------------------------------------------
$repoRoot  = Split-Path -Parent $MyInvocation.MyCommand.Definition
$venvDir   = Join-Path $repoRoot '.venv'
$docsDir   = Join-Path $repoRoot 'docs'
$pdfTarget = 'E:\pdf\python_handbook.pdf'

# ---------------------------------------------------------
# Helper – run a command and abort on failure
# ---------------------------------------------------------
function Invoke-Cmd {
    param([string]$cmd, [string]$cwd = $repoRoot)
    Write-Host "`n>>> $cmd" -ForegroundColor Cyan
    $proc = Start-Process pwsh -ArgumentList "-NoProfile -Command `"$cmd`"" -WorkingDirectory $cwd -Wait -PassThru
    if ($proc.ExitCode -ne 0) { throw "Command failed (exit $($proc.ExitCode)): $cmd" }
}

# ---------------------------------------------------------
# 1️⃣  Create / activate virtual environment
# ---------------------------------------------------------
if (-not (Test-Path $venvDir)) {
    Write-Host "Creating virtual environment..." -ForegroundColor Green
    Invoke-Cmd "python -m venv .venv"
}
. (Join-Path $venvDir 'Scripts\Activate.ps1')

# ---------------------------------------------------------
# 2️⃣  Install Python build dependencies (once)
# ---------------------------------------------------------
Write-Host "Installing Python dependencies..." -ForegroundColor Green
Invoke-Cmd "pip install --upgrade pip"
Invoke-Cmd "pip install sphinx sphinx-book-theme myst-parser pytest pytest-doctestplus"

# ---------------------------------------------------------
# 3️⃣  Run the doctest suite (optional but recommended)
# ---------------------------------------------------------
Write-Host "Running doctests..." -ForegroundColor Green
Invoke-Cmd "pytest --doctest-modules docs/"

# ---------------------------------------------------------
# 4️⃣  Generate LaTeX sources with Sphinx
# ---------------------------------------------------------
Write-Host "Building LaTeX sources..." -ForegroundColor Green
Invoke-Cmd "python -m sphinx -M latexpdf . _build" -cwd $docsDir

# ---------------------------------------------------------
# 5️⃣  Compile PDF with latexmk (runs xelatex as many times as needed)
# ---------------------------------------------------------
$latexDir = Join-Path $docsDir '_build\latex'
Write-Host "Compiling PDF with latexmk..." -ForegroundColor Green
Invoke-Cmd "latexmk -pdf -xelatex -interaction=nonstopmode python_handbook.tex" -cwd $latexDir

# ---------------------------------------------------------
# 6️⃣  Copy the PDF to the requested location
# ---------------------------------------------------------
$pdfSource = Join-Path $latexDir 'python_handbook.pdf'
if (Test-Path $pdfSource) {
    Write-Host "Copying PDF to $pdfTarget ..." -ForegroundColor Green
    $destDir = Split-Path -Parent $pdfTarget
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
    Copy-Item -Path $pdfSource -Destination $pdfTarget -Force
    Write-Host "`n✅  PDF ready at $pdfTarget" -ForegroundColor Green
}
else {
    throw "PDF not found at $pdfSource – the LaTeX build likely failed."
}