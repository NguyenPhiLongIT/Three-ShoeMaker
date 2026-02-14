import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../../data/three_shoemaker.db')

# Ensure data directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    """Initialize database tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wiki_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            image_path TEXT,
            tags TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trade_indicators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT,
            rating INTEGER,
            description TEXT,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def seed_data():
    """Add sample trading data."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM wiki_knowledge')
    if cursor.fetchone()[0] > 0:
        conn.close()
        return
    
    # Seed wiki_knowledge
    wiki_data = [
        ('RSI - Relative Strength Index', 'RSI là chỉ số động lượng đo lường tốc độ và độ lớn của biến động giá. Giá trị 70+ là overbought, <30 là oversold.', 'data/images/rsi.png', 'momentum,technical,indicator'),
        ('MACD - Moving Average Convergence Divergence', 'MACD là chỉ số kỹ thuật dùng để xác định xu hướng giá. Tạo bởi 3 đường: MACD, Signal, Histogram.', 'data/images/macd.png', 'trend,technical,indicator'),
        ('Nến Nhật (Candlestick)', 'Nến Nhật thể hiện OHLC (Open, High, Low, Close) trong một khoảng thời gian. Các pattern: Doji, Hammer, Engulfing.', 'data/images/candlestick.png', 'chart,pattern,japanese'),
    ]
    cursor.executemany(
        'INSERT INTO wiki_knowledge (title, content, image_path, tags) VALUES (?, ?, ?, ?)',
        wiki_data
    )
    
    # Seed trade_indicators
    indicator_data = [
        ('Bollinger Bands', 'BB = SMA(20) ± 2*StdDev\nUsed for volatility analysis', 5, 'Volatility analysis tool', 'data/images/bollinger.png'),
        ('Stochastic Oscillator', '%K = (Close - Low14) / (High14 - Low14) * 100\nIdentify overbought/oversold', 4, 'Momentum indicator', 'data/images/stochastic.png'),
        ('Volume Weighted Average Price', 'VWAP = Σ(Price × Volume) / Σ(Volume)\nUsed in institutional trading', 5, 'Volume-based indicator', 'data/images/vwap.png'),
    ]
    cursor.executemany(
        'INSERT INTO trade_indicators (name, code, rating, description, image_path) VALUES (?, ?, ?, ?, ?)',
        indicator_data
    )
    
    conn.commit()
    conn.close()
