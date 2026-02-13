# Phase 2 Todo App - Quick Deployment Guide

## Prerequisites
- GitHub account
- Vercel account (free)
- Render account (free) or Railway
- Neon PostgreSQL database (already configured)

## Quick Deploy Steps

### 1. Deploy Frontend to Vercel (5 minutes)

**Option A: Via Vercel Dashboard (Recommended)**
1. Go to https://vercel.com/new
2. Import repository: `fatimaibrahim27/TODO-HAKATHON-II`
3. Configure:
   - **Root Directory**: `frontend`
   - **Framework**: Next.js (auto-detected)
4. Add Environment Variable:
   - `NEXT_PUBLIC_API_BASE_URL` = `https://your-backend-url.onrender.com` (add after backend deployment)
5. Click **Deploy**
6. Save your Vercel URL (e.g., `https://todo-app-phase2.vercel.app`)

**Option B: Via CLI**
```bash
cd D:/hackathon-2/TODO-HAKATHON-II
npm install -g vercel
vercel login
vercel --prod
```

### 2. Deploy Backend to Render (10 minutes)

1. Go to https://render.com/
2. Click **New +** → **Web Service**
3. Connect GitHub: `fatimaibrahim27/TODO-HAKATHON-II`
4. Configure:
   - **Name**: `todo-api-phase2`
   - **Root Directory**: `backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variables:
   ```
   DATABASE_URL=postgresql://neondb_owner:YOUR_PASSWORD@ep-YOUR-ENDPOINT.aws.neon.tech/neondb?sslmode=require
   SECRET_KEY=your-super-secret-key-change-in-production-min-32-chars-here-now
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   FRONTEND_URL=https://your-vercel-app.vercel.app
   ```
6. Click **Create Web Service**
7. Wait for deployment (~5-10 minutes)
8. Copy your Render URL (e.g., `https://todo-api-phase2.onrender.com`)

### 3. Update Frontend Environment Variable

1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Update `NEXT_PUBLIC_API_BASE_URL` with your Render backend URL
3. Redeploy: Go to Deployments → Click "..." → Redeploy

### 4. Test Your Deployment

1. Visit your Vercel URL
2. Register a new account
3. Login
4. Create a todo item
5. Test CRUD operations

## Environment Variables Summary

### Frontend (Vercel)
```
NEXT_PUBLIC_API_BASE_URL=https://todo-api-phase2.onrender.com
```

### Backend (Render)
```
DATABASE_URL=postgresql://neondb_owner:...@ep-....aws.neon.tech/neondb?sslmode=require
SECRET_KEY=your-super-secret-key-change-in-production-min-32-chars-here-now
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FRONTEND_URL=https://todo-app-phase2.vercel.app
```

## Troubleshooting

### Frontend shows "API connection failed"
- Check `NEXT_PUBLIC_API_BASE_URL` is set correctly in Vercel
- Verify backend is running on Render
- Check browser console for CORS errors

### Backend CORS errors
- Ensure `FRONTEND_URL` is set in Render environment variables
- Check Render logs for errors

### Database connection errors
- Verify `DATABASE_URL` is correct in Render
- Check Neon database is active
- Ensure `?sslmode=require` is in connection string

## Deployment URLs

After deployment, your app will be available at:
- **Frontend**: https://your-app.vercel.app
- **Backend**: https://your-api.onrender.com
- **Database**: Neon PostgreSQL

## Notes

- Render free tier may have cold starts (first request takes ~30 seconds)
- Vercel deployments are instant
- Both services auto-deploy on git push to main branch
