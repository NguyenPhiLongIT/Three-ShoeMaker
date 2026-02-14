import sqlite3
from .database import DB_PATH

def get_all_wiki():
    """Fetch all wiki knowledge entries."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM wiki_knowledge ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def get_wiki_by_id(wiki_id):
    """Fetch a single wiki article by ID."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM wiki_knowledge WHERE id = ?', (wiki_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row) if row else None
