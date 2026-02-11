# Todo Full-Stack Application - Phase 2

This is the Phase 2 implementation of the Todo application, featuring a complete full-stack web application built with Next.js, FastAPI, and Neon PostgreSQL.

## Architecture

- **Frontend**: Next.js 14+ with App Router, TypeScript, Tailwind CSS
- **Backend**: FastAPI with Pydantic validation, SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens with secure HttpOnly cookie storage
- **Security**: bcrypt password hashing, input validation, SQL injection prevention

## Features

### Authentication
- User registration with email validation
- Secure login with JWT tokens
- Protected routes and API endpoints
- Secure logout functionality

### Todo Management
- Create, read, update, and delete todos
- Mark todos as complete/incomplete
- View all user's todos in a dashboard
- Due date support for todos
- Full CRUD operations with proper authorization

### Security Features
- Passwords hashed with bcrypt
- JWT tokens for session management
- Input validation and sanitization
- Authorization checks on all protected endpoints
- Prevention of SQL injection through ORM usage

## Project Structure

```
TODO-HAKATHON-II/
├── backend/
│   ├── src/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── models/              # SQLModel database models (User, Todo, Token)
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   ├── routers/             # API route handlers (auth, todos)
│   │   ├── database/            # Database connection and session management
│   │   ├── auth/                # Authentication utilities and middleware
│   │   └── utils/               # Helper functions
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/                 # Next.js App Router pages
│   │   │   ├── (auth)/          # Authentication pages (login, register)
│   │   │   ├── dashboard/       # Protected dashboard with todo features
│   │   │   └── globals.css      # Global styles
│   │   ├── components/          # Reusable React components
│   │   ├── lib/                 # Utilities and constants (auth context)
│   │   └── types/               # TypeScript type definitions
│   ├── package.json
│   └── next.config.js
├── specs/                       # Specification documents
│   └── 4-todo-fullstack-app/
└── .env                         # Environment variables
```

## Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL-compatible database (Neon recommended)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables in a `.env` file:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
SECRET_KEY=your-super-secret-key-here-changeme-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Start the backend server:
```bash
uvicorn src.main:app --reload --port 8000
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file with:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

4. Start the development server:
```bash
npm run dev
```

### Access the Application

- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs
- Backend API: http://localhost:8000/api

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login existing user
- `GET /api/auth/me` - Get current user info

### Todos
- `GET /api/todos` - Get user's todos
- `POST /api/todos` - Create new todo
- `PUT /api/todos/{id}` - Update todo
- `DELETE /api/todos/{id}` - Delete todo
- `PATCH /api/todos/{id}/complete` - Mark todo as complete/incomplete

## Development

### Running Backend Tests
```bash
cd backend
pytest
```

### Running Frontend Tests
```bash
cd frontend
npm test
```

## Security Considerations

1. **Authentication**: All API endpoints requiring authentication use JWT tokens
2. **Authorization**: Users can only access their own data
3. **Input Validation**: All inputs are validated using Pydantic schemas
4. **Password Security**: Passwords are hashed using bcrypt
5. **SQL Injection Prevention**: Using SQLModel ORM prevents SQL injection
6. **CORS**: Properly configured to prevent cross-origin attacks

## Next Steps

- Implement refresh token functionality
- Add email verification for user registration
- Implement password reset functionality
- Add more advanced todo features (categories, tags, sharing)
- Set up automated testing pipeline
- Deploy to production environment