# Deployment Guide - Phase 2 Todo App

## Quick Deploy Options

### Option 1: Vercel (Frontend) + Railway (Backend) + Neon (Database)

#### 1. Deploy Database (Neon - Free)

1. Go to https://neon.tech
2. Sign up and create a new project
3. Copy the connection string (looks like: `postgresql://user:pass@host/db`)
4. Save it for backend deployment

#### 2. Deploy Backend (Railway - Free tier)

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Set root directory to `backend`
5. Add environment variables:
   ```
   DATABASE_URL=<your-neon-connection-string>
   SECRET_KEY=<generate-random-string>
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
6. Set start command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
7. Deploy and copy the public URL

#### 3. Deploy Frontend (Vercel - Free)

1. Go to https://vercel.com
2. Click "New Project" → Import from GitHub
3. Select your repository
4. Set root directory to `frontend`
5. Add environment variable:
   ```
   NEXT_PUBLIC_API_BASE_URL=<your-railway-backend-url>
   ```
6. Deploy

### Option 2: Render (All-in-One)

#### 1. Database (Render PostgreSQL - Free)

1. Go to https://render.com
2. Create new PostgreSQL database
3. Copy internal connection string

#### 2. Backend (Render Web Service)

1. Create new Web Service
2. Connect GitHub repo
3. Set:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables (same as above)
5. Deploy and copy URL

#### 3. Frontend (Render Static Site)

1. Create new Static Site
2. Set:
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `.next`
3. Add environment variable with backend URL
4. Deploy

## Environment Variables Reference

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@host:5432/database
SECRET_KEY=your-super-secret-key-minimum-32-characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_BASE_URL=https://your-backend-url.com
```

## Post-Deployment Checklist

- [ ] Backend health check: `https://your-backend-url.com/health`
- [ ] Frontend loads correctly
- [ ] User registration works
- [ ] User login works
- [ ] Todo CRUD operations work
- [ ] Update CORS in backend to allow only your frontend domain

## Troubleshooting

### Backend Issues
- Check logs in Railway/Render dashboard
- Verify DATABASE_URL is correct
- Ensure all dependencies in requirements.txt

### Frontend Issues
- Check browser console for errors
- Verify NEXT_PUBLIC_API_BASE_URL is set
- Check Network tab for API call failures

### Database Issues
- Verify connection string format
- Check if database is active
- Tables are created automatically on first run

## Security Notes for Production

1. **Update CORS**: In `backend/src/main.py`, change:
   ```python
   allow_origins=["https://your-frontend-domain.com"]
   ```

2. **Generate Strong SECRET_KEY**:
   ```python
   import secrets
   print(secrets.token_urlsafe(32))
   ```

3. **Use HTTPS**: Ensure both frontend and backend use HTTPS

4. **Environment Variables**: Never commit .env files to git

## Cost Estimate

- **Free Tier (Recommended for testing)**:
  - Neon Database: Free (0.5GB storage)
  - Railway Backend: Free (500 hours/month)
  - Vercel Frontend: Free (unlimited)

- **Paid Tier (Production)**:
  - Neon: $19/month (3GB storage)
  - Railway: $5/month (8GB RAM)
  - Vercel: Free (sufficient for most cases)

## Support

For issues, check:
1. Application logs in deployment platform
2. Browser console (F12)
3. Network tab for API errors
4. Database connection status
