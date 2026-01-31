9iiiiiiiiQA# Game Challenge 01 - Environment Setup Script for Windows (PowerShell)
# This script sets up the Python environment for students

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "          GAME CHALLENGE 01 - ENVIRONMENT SETUP" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to close"
    exit 1
}

Write-Host ""

# Check if pip is available
try {
    $pipVersion = pip --version 2>&1
    Write-Host "[OK] pip is available: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] pip is not available" -ForegroundColor Red
    Write-Host "Please reinstall Python and ensure pip is selected during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to close"
    exit 1
}

Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Cyan
if (Test-Path "venv") {
    Write-Host "[INFO] Virtual environment already exists" -ForegroundColor Yellow
} else {
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to close"
        exit 1
    }
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}

Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to activate virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to close"
    exit 1
}
Write-Host "[OK] Virtual environment activated" -ForegroundColor Green

Write-Host ""

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip | Out-Null
Write-Host "[OK] pip upgraded" -ForegroundColor Green

Write-Host ""

# Verify setup
Write-Host "Verifying setup..." -ForegroundColor Cyan
$pythonPath = python -c "import sys; print(sys.executable)"
Write-Host "[OK] Python executable: $pythonPath" -ForegroundColor Green

Write-Host ""

# Install dependencies from requirements.txt
Write-Host "Installing dependencies..." -ForegroundColor Cyan
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt | Out-Null
    Write-Host "[OK] Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "[WARNING] requirements.txt not found, skipping dependency installation" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "          SETUP COMPLETED SUCCESSFULLY!" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Open this folder in VSCode" -ForegroundColor White
Write-Host "2. Select the Python interpreter from the virtual environment" -ForegroundColor White
Write-Host "   - Press Ctrl+Shift+P and search for 'Python: Select Interpreter'" -ForegroundColor White
Write-Host "   - Choose the one that says '(venv)'" -ForegroundColor White
Write-Host "3. Start coding your game in game.py or main.py" -ForegroundColor White
Write-Host ""
Write-Host "To run your script after setup:" -ForegroundColor Yellow
Write-Host "   - Activate the environment first: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   - Then run: python your_script.py" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to close"
