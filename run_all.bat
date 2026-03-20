@echo off
echo =======================================================
echo     Lumina AI - Image Generator Startup Script
echo =======================================================

echo.
echo [1] Checking and installing Python Backend Requirements...
cd backend
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing backend requirements! Make sure Python is installed.
    pause
    exit /b
)

echo.
echo [2] Starting FastAPI Backend on Port 8000...
start cmd /k "title Lumina AI Backend API && python -m uvicorn main:app --reload"

echo.
echo [3] Installing React Frontend Modules...
cd ../image-generator
call npm install
if %errorlevel% neq 0 (
    echo Error installing frontend dependencies! Make sure Node.js is installed.
    pause
    exit /b
)

echo.
echo [4] Starting React Frontend on Port 3000...
start cmd /k "title Lumina AI Frontend UI && npm start"

echo.
echo All services are starting! Check the two new command prompt windows.
echo The React frontend will automatically open in your web browser.
pause
