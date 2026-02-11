# 🚀 HOW TO RUN YOUR TODO WEBSITE

## ✅ Everything is Ready! Follow These 2 Steps:

### STEP 1: Start Backend Server

Open **Command Prompt** or **PowerShell** and run:

```bash
cd C:\Users\user\OneDrive\Desktop\TODO-HAKATHON-II\backend
venv\Scripts\activate
uvicorn src.main:app --reload --port 8000
```

**OR** Simply double-click: `START_BACKEND.bat`

✅ Backend will start at: **http://localhost:8000**
✅ API Documentation: **http://localhost:8000/docs**

---

### STEP 2: Start Frontend Server

Open a **NEW** Command Prompt/PowerShell window and run:

```bash
cd C:\Users\user\OneDrive\Desktop\TODO-HAKATHON-II\frontend
npm run dev
```

**OR** Simply double-click: `START_FRONTEND.bat`

✅ Frontend will start at: **http://localhost:3000**

---

## 🎯 Using Your Website

1. **Open your browser** and go to: **http://localhost:3000**

2. **Register a new account:**
   - Click "Get started"
   - Enter email: `test@example.com`
   - Enter password: `password123`
   - Click "Sign up"

3. **You'll be automatically logged in** and redirected to your dashboard

4. **Add todos:**
   - Type in the input field
   - Click "Add" button
   - Your todo appears instantly!

5. **Manage todos:**
   - ✅ Click checkbox to mark complete/incomplete
   - 🗑️ Click "Delete" to remove a todo
   - All changes save automatically

6. **Logout:**
   - Click "Logout" button in top right corner

---

## 🎉 Your Hackathon Project is LIVE!

**What's Working:**
- ✅ User Registration & Login
- ✅ JWT Authentication
- ✅ Create Todos
- ✅ Toggle Todo Completion
- ✅ Delete Todos
- ✅ User-specific data (each user sees only their todos)
- ✅ Responsive design
- ✅ Loading states
- ✅ Error handling

**Tech Stack:**
- Frontend: Next.js 14 + React + TypeScript + Tailwind CSS
- Backend: FastAPI + SQLModel + SQLite
- Auth: JWT tokens with secure password hashing

**Database:**
- Using SQLite (file: `backend/todo.db`)
- No PostgreSQL setup needed!
- All data persists between sessions

---

## 🔧 Troubleshooting

**Backend won't start?**
- Make sure you're in the backend directory
- Activate virtual environment: `venv\Scripts\activate`
- Check if port 8000 is free

**Frontend won't start?**
- Make sure you're in the frontend directory
- Check if port 3000 is free
- Try: `npm install` first if needed

**Can't login?**
- Make sure backend is running first (http://localhost:8000)
- Check browser console (F12) for errors
- Try registering a new account

---

## 📱 Demo Screenshots

**Home Page:** Clean landing page with "Get started" button
**Register:** Simple email + password registration
**Dashboard:** Your personal todo list with add/delete/toggle features
**Responsive:** Works on desktop, tablet, and mobile

---

## 🎓 Phase II Hackathon - COMPLETE! ✅

Your full-stack todo application is ready for demonstration!

**GitHub Repository:** https://github.com/fatimaibrahim27/TODO-HAKATHON-II

All code has been committed and pushed to the main branch.
