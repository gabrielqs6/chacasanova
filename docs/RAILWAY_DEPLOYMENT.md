# 🚂 Railway Deployment Guide

This guide will help you deploy the "Chá de Casa Nova" web app to Railway.

## 🎯 Prerequisites

- A [GitHub](https://github.com) account
- A [Railway](https://railway.app) account (free tier available)
- Git installed on your computer

## 📦 Step 1: Prepare Your Repository

### 1.1 Initialize Git (if not already done)

```bash
cd casa-nova
git init
```

### 1.2 Add a .gitignore file

The project already includes a `.gitignore` file with:
```
*.db
__pycache__/
*.pyc
.env
venv/
.vscode/
```

This ensures the database and virtual environment are not committed.

### 1.3 Commit Your Code

```bash
git add .
git commit -m "Initial commit: Chá de Casa Nova web app"
```

### 1.4 Create a GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository (e.g., `casa-nova`)
3. **Don't** initialize with README (we already have one)

### 1.5 Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/casa-nova.git
git branch -M main
git push -u origin main
```

## 🚀 Step 2: Deploy to Railway

### 2.1 Create a Railway Account

1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub (easiest option)

### 2.2 Create a New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your repositories (if first time)
4. Select your `casa-nova` repository

### 2.3 Railway Auto-Detection

Railway will automatically detect:
- ✅ Python project (from `runtime.txt`)
- ✅ Dependencies (from `requirements.txt`)
- ✅ Start command (from `Procfile`)

The app will start deploying immediately!

## ⚙️ Step 3: Configure Environment Variables

### 3.1 Add Variables

1. In Railway dashboard, click on your project
2. Go to the **"Variables"** tab
3. Add the following:

| Variable | Value | Description |
|----------|-------|-------------|
| `ADMIN_KEY` | `your-secure-key-123` | Admin panel access key |
| `SECRET_KEY` | `random-secret-key-456` | Flask secret key |

**Security Tip:** Use a password generator for these values!

### 3.2 Generate Secure Keys

You can generate secure keys using Python:

```python
import secrets
print(secrets.token_urlsafe(32))
```

Or online at: [RandomKeygen](https://randomkeygen.com/)

## 🌐 Step 4: Get Your Public URL

### 4.1 Generate a Domain

1. In Railway dashboard, click **"Settings"**
2. Scroll to **"Domains"**
3. Click **"Generate Domain"**
4. Railway will give you a URL like: `https://casa-nova-production-xxxx.up.railway.app`

### 4.2 Custom Domain (Optional)

If you have a custom domain:
1. Click **"Custom Domain"**
2. Add your domain (e.g., `chacasanova.com`)
3. Update your DNS settings as instructed

## 🎉 Step 5: Test Your Deployment

### 5.1 Visit Your App

Open the Railway-generated URL in your browser.

### 5.2 Test Guest Flow

1. Home page loads ✅
2. Click "Ver lista de presentes" ✅
3. View item details ✅
4. Reserve an item ✅
5. See success confirmation ✅

### 5.3 Test Admin Panel

Visit: `https://your-app.up.railway.app/admin?key=YOUR_ADMIN_KEY`

1. Add a new item ✅
2. Edit an item ✅
3. Change status ✅
4. Delete an item ✅

## 🔄 Step 6: Updating Your App

### 6.1 Make Changes Locally

Edit files as needed and test locally:
```bash
python app.py
```

### 6.2 Commit and Push

```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```

### 6.3 Auto-Deploy

Railway will automatically detect the push and redeploy! 🎯

Watch the deployment logs in the Railway dashboard.

## 📊 Monitoring & Logs

### View Logs

In Railway dashboard:
1. Click on your project
2. Go to **"Deployments"** tab
3. Click on the active deployment
4. View real-time logs

### Check Database

The SQLite database (`casa_nova.db`) is stored in Railway's persistent volume.

**Note:** Railway's free tier may restart your app, which could reset the database. For production, consider:
- Using Railway's persistent storage
- Or migrating to PostgreSQL (Railway offers this)

## 🛠️ Troubleshooting

### Issue: App crashes on startup

**Check:**
1. Deployment logs in Railway
2. Ensure `requirements.txt` has all dependencies
3. Verify `Procfile` syntax

### Issue: Database resets after restart

**Solution:** Railway's free tier uses ephemeral storage. Options:
1. Upgrade to Railway Pro for persistent volumes
2. Migrate to PostgreSQL (Railway provides free PostgreSQL)

### Issue: Admin panel not working

**Check:**
1. Environment variable `ADMIN_KEY` is set correctly
2. Using correct URL: `/admin?key=YOUR_KEY`

### Issue: 502 Bad Gateway

**Usually means:**
- App failed to start
- Port binding issue (Railway sets PORT automatically)

**Check:** Deployment logs for errors

## 🔒 Security Best Practices

### 1. Secure Admin Key
- Use a strong, random key
- Don't share the admin URL publicly
- Change the key if compromised

### 2. Secret Key
- Never commit `.env` files with secrets
- Use Railway's environment variables

### 3. Database Backups
For production:
- Set up automated backups
- Or use Railway's PostgreSQL with backups enabled

## 💰 Railway Pricing

### Free Tier
- ✅ Good for personal projects
- ✅ $5 free credit per month
- ⚠️ App may sleep after inactivity
- ⚠️ Limited compute hours

### Pro Tier ($20/month)
- ✅ No sleeping
- ✅ More compute hours
- ✅ Persistent storage
- ✅ Priority support

## 📈 Next Steps

### Add Features
- Email notifications when items are reserved
- Export reservations to CSV
- Add photos for items
- WhatsApp sharing

### Migrate to PostgreSQL
If you need persistent data:

1. In Railway, add a **PostgreSQL** service
2. Update `app.py` to use PostgreSQL instead of SQLite
3. Install `psycopg2` in requirements.txt

### Set Up CI/CD
- Add GitHub Actions for testing
- Automated deployment on merge to main

## 🎊 Success!

Your "Chá de Casa Nova" web app is now live on Railway! 🎉

Share the URL with your guests and enjoy the event!

---

**Questions?** Check Railway's [documentation](https://docs.railway.app/) or the main [README.md](../README.md)

**Built with ❤️ for Gabriel Queiroz**
