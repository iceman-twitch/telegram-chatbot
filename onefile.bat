@echo off
echo ================================================
echo Building Executable with PyInstaller
echo ================================================
echo.

REM Check if virtual environment exists and activate it
if exist env\Scripts\activate.bat (
    call env\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found. Using system Python.
    echo.
)

REM Build the executable as a single file
echo Building bot.exe as a single file...
echo.
pyinstaller --onefile --name telegram-chatbot bot.py

echo.
echo ================================================
echo Build complete!
echo ================================================
echo.
echo Executable location: dist\telegram-chatbot.exe
echo.
echo NOTE: Make sure to copy the .env file to the same
echo directory as the executable before running it.
echo.

REM Deactivate virtual environment if it was activated
if exist env\Scripts\deactivate.bat (
    call deactivate
)

pause
