@echo off
echo ================================
echo Building Love Me Not EXE
echo ================================

cd /d "%~dp0"

:: Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed!
    echo Please download and install Python 3.11 or higher:
    echo https://www.python.org/downloads/
    pause
    exit /b
)

:: Ensure pygame-ce
pip show pygame-ce >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing pygame-ce...
    pip install pygame-ce
)

:: Ensure PyInstaller
pip show pyinstaller >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

:: Build EXE
echo Building EXE...
python -m PyInstaller --onefile --windowed --icon=assets/Art/icon.ico --add-data "assets;assets" LoveMeNot.py

echo ================================
echo Done! The EXE is inside the "dist" folder.
echo ================================
pause

