# Chá de Casa Nova - Gabriel Queiroz

A simple, elegant web application for a housewarming gift list event.

## 🎯 Project Overview

This is a mobile-first web application built for a real-life "Chá de Casa Nova" (Housewarming Gift List) event. Guests can view gift suggestions, reserve items by entering their name, and see confirmation screens. No authentication is required for guests.

**Event Details:**
- **Couple:** Gabriel Queiroz
- **Event:** Chá de Casa Nova

## 🛠️ Tech Stack

- **Backend:** Python 3.11 + Flask
- **Frontend:** Server-side rendered HTML with Jinja2 templates
- **Styling:** Tailwind CSS (via CDN)
- **Database:** SQLite (development) / PostgreSQL (production)
- **JavaScript:** Minimal vanilla JS (for modals and search)
- **Hosting:** Railway-ready

## 🗄️ Database Support

The app automatically detects the environment and uses the appropriate database:

### Development (Local)
- **SQLite** - File-based database (`casa_nova.db`)
- Auto-creates sample data for testing
- No configuration needed

### Production (Railway/Heroku)
- **PostgreSQL** - Persistent database
- Data survives across deployments
- Auto-detected via `DATABASE_URL` environment variable

**📖 See [docs/POSTGRESQL_SETUP.md](docs/POSTGRESQL_SETUP.md) for setup instructions**

## 📁 Project Structure

```
casa-nova/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment config
├── runtime.txt           # Python version specification
├── casa_nova.db          # SQLite database (auto-generated)
├── templates/
│   ├── base.html         # Base template with Tailwind CSS
│   ├── home.html         # Welcome screen
│   ├── list.html         # Gift list screen
│   ├── item_details.html # Gift details with reservation modal
│   ├── success.html      # Reservation success screen
│   ├── owned.html        # Items already owned screen
│   └── admin.html        # Admin panel for managing items
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Local Development

1. **Clone or navigate to the project directory:**
   ```bash
   cd casa-nova
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5000`

The database will be automatically created with sample data on first run.

## 📱 Features & Screens

### 1. Home / Welcome Screen (`/`)
- Event title and couple names
- Welcome message
- CTA button to view gift list

### 2. Gift List Screen (`/list`)
- Display all available and reserved items
- Each item shows:
  - Name and category
  - Status badge (Available or Reserved)
  - Reserve button for available items
- Search functionality
- Link to "Items Already Owned" page

### 3. Gift Details Screen (`/item/<id>`)
- Full item description
- Category and notes
- Large icon/illustration
- Reserve button (opens modal)

### 4. Reservation Modal
- Name input field
- Confirm and cancel buttons
- Vanilla JS modal implementation

### 5. Reservation Success Screen (`/success/<id>`)
- Success icon
- Thank you message from Gabriel Queiroz
- Back to list button

### 6. Items Already Owned Screen (`/owned`)
- List of items marked as "Já temos 💚"
- Muted/disabled styling

### 7. Admin Panel (`/admin?key=ADMIN_KEY`)
- Add new items
- Edit existing items
- Change item status (available/reserved/owned)
- Delete items
- **Access:** Requires admin key in URL

## 🔐 Admin Access

The admin panel is protected by a key parameter:

- **Default Key:** `gabrielqueiroz2026`
- **URL:** `http://localhost:5000/admin?key=gabrielqueiroz2026`

**For production:** Set the `ADMIN_KEY` environment variable to a secure value.

## 🎨 Design System

### Colors
- **Primary:** `#5A8F7B` (Green)
- **Primary Dark:** `#4A7A67`
- **Secondary:** `#A5D6A7` (Light Green)
- **Neutral:** `#F7F7F7` (Soft background)
- **Card Background:** `#FFFFFF`
- **Text Dark:** `#333333`
- **Text Gray:** `#777777`
- **Badge Green:** `#5A8F7B`
- **Badge Gray:** `#CCCCCC`

### Typography
- **Font:** Poppins (Google Fonts)
- **Heading 1:** Poppins Bold, 24px
- **Heading 2:** Poppins Semibold, 20px
- **Body Text:** Poppins Regular, 16px
- **Button Text:** Poppins Medium, 16px

### Components
- Rounded cards (`rounded-2xl`, `rounded-3xl`)
- Soft shadows
- Rounded full buttons
- Mobile-first responsive design

## 🗄️ Database Schema

### Table: `items`

| Column       | Type    | Description                              |
|-------------|---------|------------------------------------------|
| id          | INTEGER | Primary key (auto-increment)              |
| name        | TEXT    | Item name                                 |
| category    | TEXT    | Category (Cozinha, Quarto, etc.)          |
| notes       | TEXT    | Additional details, color, size, etc.     |
| status      | TEXT    | available / reserved / owned              |
| reserved_by | TEXT    | Name of person who reserved (nullable)    |
| created_at  | TIMESTAMP | Creation timestamp                       |

## 🌐 Deployment to Railway

### Steps:

1. **Create a new project on Railway**
2. **Connect your repository or use Railway CLI**
3. **Set environment variables:**
   ```
   ADMIN_KEY=your-secure-admin-key-here
   SECRET_KEY=your-secret-flask-key-here
   ```
4. **Deploy!**

Railway will automatically detect the `Procfile` and `runtime.txt` files.

### Environment Variables

- `PORT` - Port to run the app (Railway sets this automatically)
- `ADMIN_KEY` - Admin panel access key (default: `gabrielqueiroz2026`)
- `SECRET_KEY` - Flask secret key for sessions (default: `dev-secret-key-change-in-production`)
- `DEBUG` - Set to `True` for development, `False` for production

## 📝 Routes

| Route                          | Method | Description                    |
|-------------------------------|--------|--------------------------------|
| `/`                           | GET    | Home/Welcome screen            |
| `/list`                       | GET    | Gift list screen               |
| `/item/<id>`                  | GET    | Item details                   |
| `/reserve/<id>`               | POST   | Reserve an item                |
| `/success/<id>`               | GET    | Reservation success            |
| `/owned`                      | GET    | Items already owned            |
| `/admin?key=ADMIN_KEY`        | GET    | Admin panel                    |
| `/admin/add`                  | POST   | Add new item (admin)           |
| `/admin/edit/<id>`            | POST   | Edit item (admin)              |
| `/admin/delete/<id>`          | POST   | Delete item (admin)            |

## 🧪 Testing Locally

### Sample Items

The database is pre-populated with sample items:
- Conjunto de Panelas Antiaderente (Cozinha) - Available
- Jogo de Lençóis King Size (Quarto) - Reserved
- Aspirador de Pó Vertical (Limpeza) - Available
- Liquidificador Potente (Cozinha) - Available
- Cafeteira Expresso (Cozinha) - Already Owned
- Jogo de Toalhas de Banho (Banheiro) - Already Owned
- Ferro de Passar (Lavanderia) - Already Owned

### Test Flow

1. Visit home page
2. Click "Ver lista de presentes"
3. Click on an available item
4. Click "Reservar este presente"
5. Enter a name in the modal
6. Confirm reservation
7. See success screen

## 🔧 Maintenance

### Adding Items via Admin Panel

1. Navigate to `/admin?key=YOUR_ADMIN_KEY`
2. Fill in the "Adicionar Novo Item" form
3. Submit

### Changing Item Status

Use the admin panel to:
- Mark items as "available" (resets `reserved_by`)
- Mark items as "reserved"
- Mark items as "owned" (shows on "Já temos" page)

### Viewing Reservations

In the admin panel, you can see who reserved each item in the "Reservado por" field.

## 🎉 Features

✅ Mobile-first responsive design  
✅ Simple, elegant UI following design mockup  
✅ No authentication required for guests  
✅ Instant reservation system  
✅ Admin panel for organizers  
✅ Search functionality  
✅ Status badges (Available, Reserved, Owned)  
✅ Success confirmation screens  
✅ Minimal JavaScript (vanilla only)  
✅ Server-side rendering (no SPA complexity)  
✅ SQLite database (no external DB needed)  
✅ Railway deployment ready  

## 📄 License

This is a personal project for a private event. No license.

## 💚 Contact

For questions about this project, contact Gabriel Queiroz.

---

**Built with ❤️ for Gabriel Queiroz's Chá de Casa Nova**