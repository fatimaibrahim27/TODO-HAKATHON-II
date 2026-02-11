@echo off
echo Starting Todo App Backend...
cd backend
call venv\Scripts\activate
echo Backend running at http://localhost:8000
echo API Docs at http://localhost:8000/docs
uvicorn src.main:app --reload --port 8000
