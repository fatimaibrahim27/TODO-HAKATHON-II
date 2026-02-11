# Todo Full-Stack Application

## Quick Start Guide

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL database (or use Neon Serverless)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Update `.env` file with your database URL:
```
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
```

5. Start backend server:
```bash
uvicorn src.main:app --reload --port 8000
```

Backend will run at: http://localhost:8000

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

Frontend will run at: http://localhost:3000

### Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### First Steps

1. Go to http://localhost:3000
2. Click "Get started" to register
3. Create your account
4. Start managing your todos!
