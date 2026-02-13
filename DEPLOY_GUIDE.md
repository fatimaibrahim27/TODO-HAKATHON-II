# 🚀 Complete Deployment Guide - Todo Full-Stack App

## Overview
This guide will help you deploy:
- **Backend** → Railway (Free tier)
- **Database** → Neon PostgreSQL (Free tier)
- **Frontend** → Vercel (Free tier)

Total cost: **$0/month** on free tiers!

---

## Step 1: Deploy Database (Neon PostgreSQL)

### 1.1 Create Neon Account
1. Go to https://neon.tech
2. Click "Sign Up" (use GitHub for quick signup)
3. Click "Create a project"

### 1.2 Configure Database
1. **Project name**: `todo-app-db`
2. **Region**: Choose closest to you (e.g., US East)
3. Click "Create Project"

### 1.3 Get Connection String
1. After creation, you'll see a connection string
2. Copy the **connection string** (looks like):
   ```
   postgresql://username:password@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```
3. **SAVE THIS** - you'll need it for Railway!

---

## Step 2: Deploy Backend (Railway)

### 2.1 Create Railway Account
1. Go to https://railway.app
2. Click "Login" → Sign in with GitHub
3. Authorize Railway to access your GitHub

### 2.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose repository: `fatimaibrahim27/TODO-HAKATHON-II`
4. Railway will detect your repo

### 2.3 Configure Backend Service
1. Railway will ask which service to deploy
2. Click "Add variables" before deploying
3. Add these environment variables:

   ```
   DATABASE_URL=<paste-your-neon-connection-string-here>
   SECRET_KEY=super-secret-key-change-in-production-12345-random-string
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Important**: Set the root directory:
   - Click "Settings" tab
   - Find "Root Directory"
   - Set to: `backend`

5. **Set Start Command** (if not auto-detected):
   - In Settings → "Start Command"
   - Enter: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

### 2.4 Deploy Backend
1. Click "Deploy"
2. Wait 2-3 minutes for build to complete
3. Once deployed, click "Settings" → "Networking"
4. Click "Generate Domain"
5. **COPY YOUR BACKEND URL** (e.g., `https://your-app.railway.app`)
6. **SAVE THIS** - you'll need it for Vercel!

### 2.5 Test Backend
1. Open your backend URL in browser
2. You should see: `{"message": "Todo API is running"}`
3. Test API docs: `https://your-app.railway.app/docs`

---

## Step 3: Deploy Frontend (Vercel)

### 3.1 Create Vercel Account
1. Go to https://vercel.com
2. Click "Sign Up" → Continue with GitHub
3. Authorize Vercel

### 3.2 Import Project
1. Click "Add New..." → "Project"
2. Find and select: `TODO-HAKATHON-II`
3. Click "Import"

### 3.3 Configure Frontend
1. **Framework Preset**: Next.js (auto-detected)
2. **Root Directory**: Click "Edit" → Set to `frontend`
3. **Build Command**: `npm run build` (auto-filled)
4. **Output Directory**: `.next` (auto-filled)

### 3.4 Add Environment Variable
1. Expand "Environment Variables" section
2. Add variable:
   - **Name**: `NEXT_PUBLIC_API_BASE_URL`
   - **Value**: `<your-railway-backend-url>` (from Step 2.4)
   - Example: `https://your-app.railway.app`
3. Click "Add"

### 3.5 Deploy Frontend
1. Click "Deploy"
2. Wait 2-3 minutes for build
3. Once complete, you'll see "Congratulations!"
4. Click "Visit" to open your deployed app

---

## Step 4: Update Backend CORS (Important!)

### 4.1 Get Your Vercel URL
1. Your Vercel URL will be like: `https://your-app.vercel.app`
2. Copy this URL

### 4.2 Update Backend Code
1. Go to Railway dashboard
2. Click on your backend service
3. Click "Variables" tab
4. Add new variable:
   - **Name**: `FRONTEND_URL`
   - **Value**: `https://your-app.vercel.app`
5. Click "Add"
6. Service will automatically redeploy

---

## Step 5: Test Your Deployed App! 🎉

### 5.1 Open Your App
1. Go to your Vercel URL: `https://your-app.vercel.app`
2. You should see the landing page

### 5.2 Test Registration
1. Click "Get started"
2. Enter email: `test@example.com`
3. Enter password: `Test123!`
4. Click "Sign up"
5. You should be redirected to dashboard

### 5.3 Test Todo Features
1. Add a todo: "Deploy my app ✅"
2. Click checkbox to mark complete
3. Click "Delete" to remove
4. Logout and login again - your todos persist!

---

## 🎯 Deployment Checklist

- [ ] Neon database created and connection string saved
- [ ] Railway backend deployed with environment variables
- [ ] Backend URL generated and tested
- [ ] Vercel frontend deployed with backend URL
- [ ] CORS updated with frontend URL
- [ ] Registration works
- [ ] Login works
- [ ] Todos can be created
- [ ] Todos can be toggled
- [ ] Todos can be deleted

---

## 📊 Your Deployed URLs

After deployment, save these:

```
Frontend (Vercel): https://your-app.vercel.app
Backend (Railway): https://your-app.railway.app
Database (Neon): ep-xxx.us-east-2.aws.neon.tech
```

---

## 🔧 Troubleshooting

### Frontend shows "Failed to load todos"
- Check if backend URL is correct in Vercel environment variables
- Verify backend is running: visit `https://your-backend.railway.app/health`
- Check browser console (F12) for errors

### Backend deployment fails
- Check Railway logs: Dashboard → Service → "Deployments" → Click failed deployment
- Verify all environment variables are set
- Ensure root directory is set to `backend`

### Database connection errors
- Verify DATABASE_URL is correct in Railway
- Check Neon dashboard - database should be "Active"
- Ensure connection string includes `?sslmode=require`

### CORS errors in browser
- Add FRONTEND_URL environment variable to Railway
- Redeploy backend after adding variable
- Clear browser cache and try again

---

## 💰 Free Tier Limits

**Neon (Database)**:
- 0.5 GB storage
- 1 project
- Unlimited queries

**Railway (Backend)**:
- $5 free credit/month
- ~500 hours runtime
- 1 GB RAM

**Vercel (Frontend)**:
- Unlimited deployments
- 100 GB bandwidth/month
- Automatic HTTPS

---

## 🔐 Security Recommendations

### For Production:
1. **Generate strong SECRET_KEY**:
   ```python
   import secrets
   print(secrets.token_urlsafe(32))
   ```

2. **Update CORS** to only allow your frontend:
   - In Railway, update FRONTEND_URL to your exact Vercel domain

3. **Enable HTTPS** (automatic on Vercel & Railway)

4. **Never commit** `.env` files to git

---

## 🎓 Next Steps

After successful deployment:
1. Share your app URL with friends!
2. Add custom domain (optional)
3. Monitor usage in Railway/Vercel dashboards
4. Add more features (categories, due dates, etc.)

---

## 📞 Support

**Railway Issues**: https://railway.app/help
**Vercel Issues**: https://vercel.com/support
**Neon Issues**: https://neon.tech/docs

**Your GitHub Repo**: https://github.com/fatimaibrahim27/TODO-HAKATHON-II

---

## 🎉 Congratulations!

You've successfully deployed a full-stack application with:
- ✅ Next.js frontend
- ✅ FastAPI backend
- ✅ PostgreSQL database
- ✅ JWT authentication
- ✅ CRUD operations
- ✅ Production-ready deployment

**Your app is now live on the internet!** 🚀
