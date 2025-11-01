@echo off
echo ================================================
echo Creating Python Virtual Environment
echo ================================================
echo.

REM Check if Python 3.9 is available
python --version
echo.

REM Create virtual environment in 'env' folder
echo Creating virtual environment in 'env' folder...
python -m venv env

if exist env\Scripts\activate.bat (
    echo.
    echo ================================================
    echo Virtual environment created successfully!
    echo ================================================
    echo.
    echo To activate the environment, run:
    echo   env\Scripts\activate
    echo.
    echo To install dependencies, run:
    echo   env\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
) else (
    echo.
    echo ================================================
    echo ERROR: Failed to create virtual environment!
    echo ================================================
    echo.
)

pause
