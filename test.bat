@echo off
echo ================================================
echo Telegram Chatbot - Test Runner
echo ================================================
echo.

REM Check if virtual environment exists
if not exist env\Scripts\activate.bat (
    echo ERROR: Virtual environment not found!
    echo Please run env.bat first to create the virtual environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call env\Scripts\activate.bat
echo.

REM Check if .env file exists
if not exist .env (
    echo WARNING: .env file not found!
    echo Please create a .env file with your BOT_TOKEN.
    echo You can copy .env.example and add your token.
    echo.
    call deactivate
    pause
    exit /b 1
)

REM Run the bot
echo Starting Telegram bot...
echo Press Ctrl+C to stop the bot
echo.
python bot.py

REM Deactivate virtual environment after program ends
echo.
echo ================================================
echo Bot stopped. Deactivating virtual environment...
echo ================================================
call deactivate

echo.
echo Virtual environment deactivated.
pause
