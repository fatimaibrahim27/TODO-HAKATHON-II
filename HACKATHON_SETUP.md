# Phase II Hackathon - Todo Full-Stack Application

## ✅ Project Status: READY TO RUN

This is a complete full-stack todo application built for the Phase II Hackathon.

## 🚀 Quick Start (2 Steps)

### Step 1: Start Backend
Open a terminal and run:
```bash
cd backend
venv\Scripts\activate
uvicorn src.main:app --reload --port 8000
```

**OR** double-click: `START_BACKEND.bat`

Backend will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Step 2: Start Frontend
Open a NEW terminal and run:
```bash
cd frontend
npm run dev
```

**OR** double-click: `START_FRONTEND.bat`

Frontend will be available at: http://localhost:3000

## 🎯 Demo Instructions

1. Open http://localhost:3000
2. Click "Get started" to register a new account
3. Enter email and password (e.g., test@example.com / password123)
4. You'll be automatically logged in and redirected to dashboard
5. Add todos using the input field
6. Toggle completion status by clicking the checkbox
7. Delete todos using the Delete button
8. Logout using the button in the top right

## 🛠️ Tech Stack

**Frontend:**
- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS
- Axios for API calls

**Backend:**
- FastAPI (Python)
- SQLModel ORM
- SQLite Database (auto-configured for demo)
- JWT Authentication
- Uvicorn ASGI server

## 📁 Project Structure

```
TODO-HAKATHON-II/
├── backend/
│   ├── src/
│   │   ├── auth/          # JWT authentication
│   │   ├── database/      # Database config (SQLite fallback)
│   │   ├── models/        # User & Todo models
│   │   ├── routers/       # API routes (/api/auth, /api/todos)
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── utils/         # Helper functions
│   │   └── main.py        # FastAPI app
│   ├── venv/              # Python virtual environment
│   ├── requirements.txt   # Python dependencies
│   └── todo.db           # SQLite database (created on first run)
├── frontend/
│   ├── src/
│   │   ├── app/           # Next.js pages (App Router)
│   │   ├── components/    # React components
│   │   └── lib/           # Auth utilities
│   ├── node_modules/      # Node dependencies
│   └── package.json       # Node dependencies
├── .env                   # Backend environment variables
├── START_BACKEND.bat      # Quick start script for backend
└── START_FRONTEND.bat     # Quick start script for frontend
```

## 🔐 Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT token authentication
- ✅ Protected API endpoints
- ✅ User isolation (users only see their own todos)
- ✅ CORS configuration
- ✅ Input validation

## 🔧 Configuration

### Database
Currently configured to use **SQLite** for easy local demo (no PostgreSQL setup required).

To use PostgreSQL/Neon instead:
1. Edit `.env` file
2. Uncomment and update: `DATABASE_URL=postgresql://user:pass@host:5432/dbname`

### Environment Variables

**Backend (.env):**
```env
# DATABASE_URL commented out = SQLite fallback
SECRET_KEY=super-secret-key-change-in-production-12345
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## 📋 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout user

### Todos
- `GET /api/todos` - Get all todos (user-specific)
- `POST /api/todos` - Create new todo
- `GET /api/todos/{id}` - Get specific todo
- `PUT /api/todos/{id}` - Update todo
- `PATCH /api/todos/{id}/complete` - Toggle completion
- `DELETE /api/todos/{id}` - Delete todo

## ✅ Hackathon Checklist

- ✅ Backend running on port 8000
- ✅ Frontend running on port 3000
- ✅ User registration working
- ✅ User login working
- ✅ JWT authentication implemented
- ✅ Dashboard loads user-specific todos
- ✅ Add todo functionality
- ✅ Toggle todo completion
- ✅ Delete todo functionality
- ✅ Loading states implemented
- ✅ Error handling implemented
- ✅ Responsive design
- ✅ SQLite database auto-configured
- ✅ All API routes under /api/ prefix
- ✅ User isolation enforced

## 🎓 Phase II Completion

This project represents the completion of Phase II of the Todo Hackathon:
- **Phase I**: CLI Todo Application ✅
- **Phase II**: Full-Stack Web Application ✅

Built with Claude Code following spec-driven development workflow.

## 📝 Notes

- Database file `todo.db` will be created automatically in the backend directory on first run
- All user passwords are securely hashed with bcrypt
- JWT tokens expire after 30 minutes
- Frontend uses localStorage for token persistence
- CORS is configured to allow frontend-backend communication

## 🚨 Troubleshooting

**Backend won't start:**
- Make sure virtual environment is activated: `venv\Scripts\activate`
- Check if port 8000 is available
- Verify dependencies: `pip install -r requirements.txt`

**Frontend won't start:**
- Check if port 3000 is available
- Verify dependencies: `npm install`
- Clear Next.js cache: `rm -rf .next`

**Can't login:**
- Make sure backend is running first
- Check browser console for errors
- Verify .env.local has correct API URL

## 🎉 Demo Ready!

Your hackathon project is fully configured and ready to demonstrate!
