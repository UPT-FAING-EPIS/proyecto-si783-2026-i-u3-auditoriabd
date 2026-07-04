import sys
from unittest.mock import MagicMock
import os
import sqlite3

# Mock streamlit para evitar errores de GUI al importar app.py
sys.modules['streamlit'] = MagicMock()

import app

def test_hash_password():
    # La contraseña admin123 tiene un hash SHA-256 conocido
    hash_esperado = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
    assert app.hash_password("admin123") == hash_esperado
    assert app.hash_password("test") != "test"
    assert app.hash_password("123") != app.hash_password("1234")

def test_init_db():
    app.init_db()
    assert os.path.exists("saas_admin.db")
    
    conn = sqlite3.connect('saas_admin.db')
    cursor = conn.cursor()
    
    # Verificar que las tablas fueron creadas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    assert "usuarios" in tables
    assert "registro_accesos" in tables
    assert "conexiones_guardadas" in tables
    
    # Verificar el admin por defecto
    cursor.execute("SELECT username, rol FROM usuarios WHERE username='admin'")
    resultado = cursor.fetchone()
    assert resultado is not None
    assert resultado[0] == "admin"
    assert resultado[1] == "admin"
    
    conn.close()
