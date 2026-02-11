# Quickstart Guide: Todo Full-Stack App

**Feature**: Todo Full-Stack App (specs/4-todo-fullstack-app/spec.md)
**Created**: 2026-02-06

## Prerequisites

- Node.js 18+ for frontend
- Python 3.9+ for backend
- PostgreSQL-compatible database (Neon recommended)
- Environment variables configured

## Setup Instructions

### 1. Environment Variables

Create `.env` files for both frontend and backend:

**Backend (.env)**:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

**Frontend (.env.local)**:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the backend server
uvicorn src.main:app --reload --port 8000
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

### 4. Access the Application

- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs
- Backend API: http://localhost:8000/api

## API Endpoints

### Authentication
- POST `/auth/register` - Register new user
- POST `/auth/login` - Login existing user
- POST `/auth/logout` - Logout current user
- GET `/auth/me` - Get current user info

### Todos
- GET `/todos` - Get user's todos
- POST `/todos` - Create new todo
- PUT `/todos/{id}` - Update todo
- DELETE `/todos/{id}` - Delete todo
- PATCH `/todos/{id}/complete` - Mark todo as complete/incomplete

## Development

### Running Tests

**Backend**:
```bash
cd backend
pytest
```

**Frontend**:
```bash
cd frontend
npm test
```

### Database Migrations

```bash
# Generate migration after changing models
alembic revision --autogenerate -m "Migration description"

# Apply migrations
alembic upgrade head
```