# Quickstart Guide: Full-Stack Todo Web Application

## Prerequisites
- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL-compatible database (Neon PostgreSQL recommended)
- Git for version control

## Getting Started

### 1. Clone and Setup Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup (FastAPI)
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the backend:
   ```bash
   uvicorn main:app --reload
   ```

### 3. Frontend Setup (Next.js)
1. Navigate to frontend directory:
   ```bash
   cd frontend  # or cd ../frontend if you're in backend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set environment variables:
   ```bash
   cp .env.local.example .env.local
   # Edit .env.local with your configuration
   ```

4. Run the development server:
   ```bash
   npm run dev
   ```

### 4. Database Setup
1. Create a Neon PostgreSQL database account
2. Configure your database URL in backend/.env
3. Run database migrations (when available):
   ```bash
   # From backend directory
   python -m alembic upgrade head
   ```

## API Documentation
Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Project Structure
```
project-root/
├── backend/              # FastAPI application
│   ├── main.py           # Application entry point
│   ├── requirements.txt  # Python dependencies
│   ├── src/
│   │   ├── models/       # SQLModel definitions
│   │   ├── api/          # API route definitions
│   │   └── database/     # Database configuration
│   └── tests/            # Backend tests
└── frontend/             # Next.js application
    ├── src/
    │   ├── app/          # App Router pages
    │   ├── components/   # React components
    │   └── lib/          # Utilities and API clients
    ├── package.json
    └── tests/            # Frontend tests
```

## Common Commands
- Backend development: `uvicorn main:app --reload`
- Frontend development: `npm run dev`
- Backend tests: `pytest`
- Frontend tests: `npm run test`
- Format backend code: `black . && isort .`
- Format frontend code: `npm run format`

## Environment Variables
### Backend (.env)
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key (generate a strong random key)
- `ALGORITHM`: JWT algorithm (default: "HS256")
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiry time (default: 30 days)

### Frontend (.env.local)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for backend API