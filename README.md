# Todo Hackathon - Phase 2: Full-Stack Web Application

A modern, secure full-stack todo application built with Next.js, FastAPI, and PostgreSQL.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication with registration and login
- **Todo Management**: Full CRUD operations for todos
- **Real-time Updates**: Optimistic UI updates for smooth user experience
- **Responsive Design**: Beautiful UI with Tailwind CSS that works on all devices
- **Secure API**: Protected endpoints with JWT token validation
- **PostgreSQL Database**: Persistent storage with proper relationships

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** (App Router)
- **React 18**
- **TypeScript**
- **Tailwind CSS**
- **Axios** for API calls

### Backend
- **FastAPI** (Python)
- **SQLModel** (ORM)
- **PostgreSQL** (Database)
- **JWT** (Authentication)
- **Passlib** (Password hashing)
- **Uvicorn** (ASGI server)

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.9+
- PostgreSQL database (or Neon Serverless)

## 🔧 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd TODO-HAKATHON-II
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

### 4. Environment Variables

Create a `.env` file in the root directory:

```env
# Backend
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Create a `.env.local` file in the `frontend` directory:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### 5. Database Setup

```bash
# Create PostgreSQL database
createdb todo_db

# Tables will be created automatically on first run
```

## 🚀 Running the Application

### Start Backend (Terminal 1)

```bash
cd backend
uvicorn src.main:app --reload
```

Backend will run on: http://localhost:8000

### Start Frontend (Terminal 2)

```bash
cd frontend
npm run dev
```

Frontend will run on: http://localhost:3000

## 📱 Usage

1. Open http://localhost:3000 in your browser
2. Click "Get started" to register a new account
3. Login with your credentials
4. Start managing your todos!

## 🔐 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user
- `POST /auth/logout` - Logout user

### Todos
- `GET /todos` - Get all todos
- `POST /todos` - Create new todo
- `GET /todos/{id}` - Get specific todo
- `PUT /todos/{id}` - Update todo
- `PATCH /todos/{id}/complete` - Toggle todo completion
- `DELETE /todos/{id}` - Delete todo

## 📁 Project Structure

```
TODO-HAKATHON-II/
├── backend/
│   ├── src/
│   │   ├── auth/          # Authentication logic
│   │   ├── database/      # Database configuration
│   │   ├── models/        # SQLModel models
│   │   ├── routers/       # API routes
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── utils/         # Utility functions
│   │   └── main.py        # FastAPI app
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/           # Next.js pages
│   │   ├── components/    # React components
│   │   └── lib/           # Utilities
│   └── package.json
└── README.md
```

## 🔒 Security Features

- Password hashing with bcrypt
- JWT token authentication
- Protected API endpoints
- CORS configuration
- SQL injection prevention via ORM
- Input validation

## 🚀 Deployment

### Backend (Railway/Render/Heroku)

1. Set environment variables
2. Deploy with: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Vercel/Netlify)

1. Set `NEXT_PUBLIC_API_BASE_URL` to your backend URL
2. Deploy with: `npm run build && npm start`

### Database (Neon/Supabase)

1. Create PostgreSQL database
2. Update `DATABASE_URL` in environment variables

## 📝 License

MIT License

## 👨‍💻 Author

Todo Hackathon Project - Phase 2

## 🙏 Acknowledgments

- Built as part of Todo Hackathon
- Phase 1: CLI Todo App
- Phase 2: Full-Stack Web Application
