import sqlite3

def init_db():
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        wallet TEXT,
        balance REAL DEFAULT 0,
        referred_by INTEGER,
        joined INTEGER DEFAULT 0
    )""")
    conn.commit()
    conn.close()

def add_user(user_id, referred_by=None):
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, referred_by) VALUES (?, ?)", (user_id, referred_by))
    conn.commit()
    conn.close()

def set_joined(user_id):
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("UPDATE users SET joined=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def set_wallet(user_id, wallet):
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet, user_id))
    conn.commit()
    conn.close()

def update_balance(user_id, amount):
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("UPDATE users SET balance = balance + ? WHERE user_id=?", (amount, user_id))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("airdrop.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user
