#!/bin/bash

echo "=========================================="
echo "VERCEL DEPLOYMENT SCRIPT"
echo "=========================================="
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "[INFO] Vercel CLI not found. Installing..."
    npm install -g vercel
fi

echo "[INFO] Starting Vercel deployment..."
echo ""

# Navigate to project root
cd "$(dirname "$0")"

# Deploy to Vercel
echo "[INFO] Deploying to Vercel..."
vercel --prod

echo ""
echo "=========================================="
echo "[SUCCESS] Deployment initiated!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Copy your Vercel deployment URL"
echo "2. Deploy backend to Render (see DEPLOYMENT.md)"
echo "3. Update NEXT_PUBLIC_API_BASE_URL in Vercel dashboard"
echo "4. Update FRONTEND_URL in Render dashboard"
echo ""
