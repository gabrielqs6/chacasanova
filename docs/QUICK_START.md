# 🚀 Quick Start Guide

## Running the Application Locally

### Option 1: Using Python directly

```bash
# Navigate to the project directory
cd casa-nova

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser and visit: `http://localhost:5000`

### Option 2: Using Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🎯 Testing the Application

### Guest Flow

1. **Home Page** → Click "Ver lista de presentes"
2. **Gift List** → Browse available items
3. **Item Details** → Click "Vou levar esse 🎁" on any available item
4. **Reservation Modal** → Enter your name
5. **Success Screen** → See confirmation

### Admin Flow

1. Visit: `http://localhost:5000/admin?key=gabrielqueiroz2026`
2. Add a new item
3. Edit existing items
4. Change status (available → reserved → owned)

## 📂 Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with all routes |
| `casa_nova.db` | SQLite database (auto-created on first run) |
| `templates/` | All HTML templates |
| `requirements.txt` | Python dependencies |
| `Procfile` | Railway deployment configuration |

## 🎨 Customization

### Change Colors

Edit [templates/base.html](templates/base.html):
```javascript
colors: {
    primary: '#5A8F7B',        // Main green color
    secondary: '#A5D6A7',      // Light green
    // ... etc
}
```

### Add Sample Data

Edit the `sample_items` list in [app.py](app.py) inside the `init_db()` function.

### Change Admin Key

Set environment variable:
```bash
# Windows PowerShell
$env:ADMIN_KEY = "your-secure-key"

# Linux/macOS
export ADMIN_KEY=your-secure-key
```

## 🌐 Deploying to Railway

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### Step 2: Connect to Railway

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository

### Step 3: Set Environment Variables

In Railway dashboard, go to **Variables** and add:

```
ADMIN_KEY=your-secure-admin-key-here
SECRET_KEY=your-secret-flask-key-here
```

### Step 4: Deploy!

Railway will automatically:
- Detect Python runtime from `runtime.txt`
- Install dependencies from `requirements.txt`
- Use `Procfile` to start the app with Gunicorn

Your app will be live at: `https://your-app.up.railway.app`

## 🔧 Troubleshooting

### Issue: Database not created

**Solution:** Delete `casa_nova.db` and restart the app. It will auto-create with sample data.

### Issue: Port already in use

**Solution:** Kill the process using port 5000 or change the port:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/macOS
lsof -ti:5000 | xargs kill
```

### Issue: Module not found

**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📱 Browser Compatibility

Tested on:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (iOS/macOS)
- ✅ Mobile browsers

## 🎉 That's it!

You now have a fully functional gift list web app. Happy gifting! 💚

---

**Need help?** Check the main [README.md](README.md) for more details.
