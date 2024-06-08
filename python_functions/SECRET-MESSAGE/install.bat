@echo off

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    REM Install Python
    echo Installing Python...
    choco install python --yes
)

REM Check if pip is installed
where pip >nul 2>nul
if %errorlevel% neq 0 (
    REM Install pip
    echo Installing pip...
    choco install pip --yes
)

REM Install cryptography module
echo Installing cryptography module...
pip install cryptography

echo Installation complete.

