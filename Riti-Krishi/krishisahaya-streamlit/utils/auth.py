import streamlit as st
import sqlite3
import hashlib

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        user_type TEXT,
        soil_type TEXT,
        land_area REAL,
        irrigation_type TEXT,
        location TEXT
    )
    """)
    conn.commit()
    conn.close()

def register_user(name, email, password, farmer_data):
    init_db()
    try:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
        INSERT INTO users 
        (name, email, password, user_type, soil_type, land_area, irrigation_type, location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, email, hashed_pw,
            farmer_data["user_type"],
            farmer_data["soil_type"],
            farmer_data["land_area"],
            farmer_data["irrigation_type"],
            farmer_data["location"]
        ))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        st.error("Email already registered")
        return False
    finally:
        conn.close()

def authenticate_user(email, password):
    init_db()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hashed_pw))
    user = c.fetchone()
    conn.close()
    return bool(user)