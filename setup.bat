@echo off
REM Game Challenge 01 - Environment Setup Script for Windows
REM This script sets up the Python environment for students

echo.
echo ============================================================
echo          GAME CHALLENGE 01 - ENVIRONMENT SETUP
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    echo [OK] Python %%i found
    echo.
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    echo Please reinstall Python and ensure pip is selected during installation
    pause
    exit /b 1
) else (
    echo [OK] pip is available
    echo.
)

REM Create virtual environment
echo Creating virtual environment...
if exist venv (
    echo [INFO] Virtual environment already exists
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] pip upgraded
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Verify setup
echo Verifying setup...
python -c "import sys; print('[OK] Python executable:', sys.executable)"
if errorlevel 1 (
    echo [ERROR] Verification failed
    pause
    exit /b 1
)
echo.

REM Success message
echo ============================================================
echo          SETUP COMPLETED SUCCESSFULLY!
echo ============================================================
echo.
echo Next steps:
echo 1. Open this folder in VSCode
echo 2. Select the Python interpreter from the virtual environment
echo    - Press Ctrl+Shift+P and search for "Python: Select Interpreter"
echo    - Choose the one that says "(venv)"
echo 3. Start coding your game in game.py or main.py
echo.
echo To run your script after setup:
echo   - On Windows: venv\Scripts\python.exe your_script.py
echo   - Or activate venv first: venv\Scripts\activate.bat
echo.
pause
