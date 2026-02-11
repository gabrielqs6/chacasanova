import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
ADMIN_KEY = os.environ.get('ADMIN_KEY', 'gabrielqueiroz2026')

# Database configuration - Use PostgreSQL in production, SQLite locally
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    # Fix Railway's postgres:// to postgresql://
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    import psycopg2
    import psycopg2.extras
    USE_POSTGRES = True
else:
    USE_POSTGRES = False
    # Use absolute path to ensure database is saved in the project directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = '/data/casa_nova.db'


def get_db():
    """Connect to the database."""
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        # Use RealDictCursor for dict-like row access
        return conn
    else:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

def dict_factory(cursor, row):
    """Convert database row to dictionary."""
    if USE_POSTGRES:
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, row))
    else:
        return dict(row)

def init_db():
    """Initialize the database with the schema."""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        if USE_POSTGRES:
            # PostgreSQL syntax
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    notes TEXT,
                    suggestion_link TEXT,
                    price_estimate INTEGER,
                    status TEXT DEFAULT 'available',
                    reserved_by TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Migration: Add suggestion_link column if it doesn't exist (PostgreSQL)
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='items' AND column_name='suggestion_link'
            """)
            if not cursor.fetchone():
                cursor.execute('ALTER TABLE items ADD COLUMN suggestion_link TEXT')
            
            # Migration: Add price_estimate column if it doesn't exist (PostgreSQL)
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='items' AND column_name='price_estimate'
            """)
            if not cursor.fetchone():
                cursor.execute('ALTER TABLE items ADD COLUMN price_estimate INTEGER')
            
            # Migration: Add image_url column if it doesn't exist (PostgreSQL)
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='items' AND column_name='image_url'
            """)
            if not cursor.fetchone():
                cursor.execute('ALTER TABLE items ADD COLUMN image_url TEXT')
        else:
            # SQLite syntax
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    notes TEXT,
                    suggestion_link TEXT,
                    price_estimate INTEGER,
                    status TEXT DEFAULT 'available',
                    reserved_by TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Migration: Add suggestion_link column if it doesn't exist (SQLite)
            cursor.execute("PRAGMA table_info(items)")
            columns = [column[1] for column in cursor.fetchall()]
            if 'suggestion_link' not in columns:
                cursor.execute('ALTER TABLE items ADD COLUMN suggestion_link TEXT')
            if 'price_estimate' not in columns:
                cursor.execute('ALTER TABLE items ADD COLUMN price_estimate INTEGER')
            if 'image_url' not in columns:
                cursor.execute('ALTER TABLE items ADD COLUMN image_url TEXT')
        
        # Only add sample data in development (when using SQLite)
        if not USE_POSTGRES:
            cursor.execute('SELECT COUNT(*) as count FROM items')
            result = cursor.fetchone()
            count = result['count'] if not USE_POSTGRES else result[0]
            
            if count == 0:
                print("Banco de dados vazio. Adicionando dados de exemplo...")
                # Add sample items for local development only
                sample_items = [
                    ('Conjunto de Panelas Antiaderente', 'Cozinha', '', 'https://www.magazineluiza.com.br/panelas', 150, 'available', None),
                    ('Jogo de Lençóis King Size', 'Quarto', '', '', 80, 'reserved', 'Maria Silva'),
                    ('Aspirador de Pó Vertical', 'Limpeza', '', 'https://www.americanas.com.br/aspiradores', 200, 'available', None),
                    ('Liquidificador Potente', 'Cozinha', '', '', 120, 'available', None),
                    ('Cafeteira Expresso', 'Cozinha', '', '', 300, 'owned', None),
                    ('Jogo de Toalhas de Banho', 'Banheiro', '', '', 60, 'owned', None),
                    ('Ferro de Passar', 'Lavanderia', '', '', 90, 'owned', None),
                    ('Jogo de Pratos', 'Cozinha', '', '', 45, 'available', None),
                    ('Edredom Casal', 'Quarto', '', '', 130, 'available', None),
                    ('Mixer', 'Cozinha', '', '', 70, 'available', None),
                ]
                
                placeholder = '?' if not USE_POSTGRES else '%s'
                query = f'INSERT INTO items (name, category, notes, suggestion_link, image_url, price_estimate, status, reserved_by) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})'
                # Add None for image_url in sample items
                sample_items_with_image = [(item[0], item[1], item[2], item[3], None, item[4], item[5], item[6]) for item in sample_items]
                cursor.executemany(query, sample_items_with_image)
                print("Dados de exemplo adicionados com sucesso!")
        
        conn.commit()
    except Exception as e:
        print(f"Erro ao inicializar banco de dados: {e}")
        conn.rollback()
    finally:
        conn.close()

# Initialize database on startup
init_db()

@app.route('/')
def home():
    """Home/Welcome screen."""
    return render_template('home.html')

@app.route('/list')
def gift_list():
    """Main gift list screen showing all available and reserved items."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM items 
        WHERE status IN ('available', 'reserved')
        ORDER BY 
            CASE status 
                WHEN 'available' THEN 1 
                WHEN 'reserved' THEN 2 
            END,
            id
    ''')
    items = [dict_factory(cursor, row) for row in cursor.fetchall()]
    conn.close()
    return render_template('list.html', items=items)

@app.route('/item/<int:item_id>')
def item_details(item_id):
    """Gift details screen."""
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    cursor.execute(f'SELECT * FROM items WHERE id = {placeholder}', (item_id,))
    row = cursor.fetchone()
    item = dict_factory(cursor, row) if row else None
    conn.close()
    
    if not item:
        flash('Item não encontrado.', 'error')
        return redirect(url_for('gift_list'))
    
    return render_template('item_details.html', item=item)

@app.route('/reserve/<int:item_id>', methods=['POST'])
def reserve_item(item_id):
    """Handle reservation of an item."""
    name = request.form.get('name', '').strip()
    
    if not name:
        flash('Por favor, digite seu nome.', 'error')
        return redirect(url_for('item_details', item_id=item_id))
    
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    
    # Check if item exists and is available
    cursor.execute(f'SELECT * FROM items WHERE id = {placeholder} AND status = {placeholder}', (item_id, 'available'))
    row = cursor.fetchone()
    item = dict_factory(cursor, row) if row else None
    
    if not item:
        flash('Este item não está mais disponível.', 'error')
        conn.close()
        return redirect(url_for('gift_list'))
    
    # Reserve the item
    cursor.execute(f'''
        UPDATE items 
        SET status = 'reserved', reserved_by = {placeholder}
        WHERE id = {placeholder}
    ''', (name, item_id))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('reservation_success', item_id=item_id))

@app.route('/success/<int:item_id>')
def reservation_success(item_id):
    """Reservation success screen."""
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    cursor.execute(f'SELECT * FROM items WHERE id = {placeholder}', (item_id,))
    row = cursor.fetchone()
    item = dict_factory(cursor, row) if row else None
    conn.close()
    
    if not item:
        return redirect(url_for('gift_list'))
    
    return render_template('success.html', item=item)

@app.route('/owned')
def items_owned():
    """Screen showing items already owned."""
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    cursor.execute(f'SELECT * FROM items WHERE status = {placeholder} ORDER BY id', ('owned',))
    items = [dict_factory(cursor, row) for row in cursor.fetchall()]
    conn.close()
    return render_template('owned.html', items=items)

@app.route('/color-palette')
def color_palette():
    """Screen showing color palettes for gift inspiration."""
    return render_template('color_palette.html')

@app.route('/admin')
def admin_panel():
    """Admin panel - requires admin key."""
    key = request.args.get('key', '')
    
    if key != ADMIN_KEY:
        return 'Acesso negado. Chave de admin inválida.', 403
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items ORDER BY id')
    items = [dict_factory(cursor, row) for row in cursor.fetchall()]
    conn.close()
    
    return render_template('admin.html', items=items, admin_key=ADMIN_KEY)

@app.route('/admin/add', methods=['POST'])
def admin_add_item():
    """Add a new item (admin only)."""
    key = request.form.get('admin_key', '')
    
    if key != ADMIN_KEY:
        return 'Acesso negado', 403
    
    name = request.form.get('name', '').strip()
    category = request.form.get('category', '').strip()
    notes = request.form.get('notes', '').strip()
    suggestion_link = request.form.get('suggestion_link', '').strip()
    image_url = request.form.get('image_url', '').strip()
    price_estimate = request.form.get('price_estimate', '').strip()
    price_estimate = int(price_estimate) if price_estimate and price_estimate.isdigit() else None
    
    if not name or not category:
        flash('Nome e categoria são obrigatórios.', 'error')
        return redirect(url_for('admin_panel', key=key))
    
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    cursor.execute(f'''
        INSERT INTO items (name, category, notes, suggestion_link, image_url, price_estimate, status)
        VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, 'available')
    ''', (name, category, notes, suggestion_link, image_url, price_estimate))
    conn.commit()
    conn.close()
    
    flash('Item adicionado com sucesso!', 'success')
    return redirect(url_for('admin_panel', key=key))

@app.route('/admin/edit/<int:item_id>', methods=['POST'])
def admin_edit_item(item_id):
    """Edit an item (admin only)."""
    key = request.form.get('admin_key', '')
    
    if key != ADMIN_KEY:
        return 'Acesso negado', 403
    
    name = request.form.get('name', '').strip()
    category = request.form.get('category', '').strip()
    notes = request.form.get('notes', '').strip()
    suggestion_link = request.form.get('suggestion_link', '').strip()
    image_url = request.form.get('image_url', '').strip()
    price_estimate = request.form.get('price_estimate', '').strip()
    price_estimate = int(price_estimate) if price_estimate and price_estimate.isdigit() else None
    status = request.form.get('status', 'available')
    
    if not name or not category:
        flash('Nome e categoria são obrigatórios.', 'error')
        return redirect(url_for('admin_panel', key=key))
    
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    
    # If status is being changed to available, clear reserved_by
    if status == 'available':
        cursor.execute(f'''
            UPDATE items 
            SET name = {placeholder}, category = {placeholder}, notes = {placeholder}, suggestion_link = {placeholder}, image_url = {placeholder}, price_estimate = {placeholder}, status = {placeholder}, reserved_by = NULL
            WHERE id = {placeholder}
        ''', (name, category, notes, suggestion_link, image_url, price_estimate, status, item_id))
    else:
        cursor.execute(f'''
            UPDATE items 
            SET name = {placeholder}, category = {placeholder}, notes = {placeholder}, suggestion_link = {placeholder}, image_url = {placeholder}, price_estimate = {placeholder}, status = {placeholder}
            WHERE id = {placeholder}
        ''', (name, category, notes, suggestion_link, image_url, price_estimate, status, item_id))
    
    conn.commit()
    conn.close()
    
    flash('Item atualizado com sucesso!', 'success')
    return redirect(url_for('admin_panel', key=key))

@app.route('/admin/delete/<int:item_id>', methods=['POST'])
def admin_delete_item(item_id):
    """Delete an item (admin only)."""
    key = request.form.get('admin_key', '')
    
    if key != ADMIN_KEY:
        return 'Acesso negado', 403
    
    conn = get_db()
    cursor = conn.cursor()
    placeholder = '?' if not USE_POSTGRES else '%s'
    cursor.execute(f'DELETE FROM items WHERE id = {placeholder}', (item_id,))
    conn.commit()
    conn.close()
    
    flash('Item removido com sucesso!', 'success')
    return redirect(url_for('admin_panel', key=key))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', 'False') == 'True')
