import sqlite3
from config import DATABASE

def crear_base_datos():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Crear tabla de clientes
    c.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        correo TEXT,
        telefono TEXT
    )
    ''')

    # Crear tabla de distritos
    c.execute('''
    CREATE TABLE IF NOT EXISTS distritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        provincia TEXT
    )
    ''')

    conn.commit()
    conn.close()

def obtener_clientes():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    conn.close()
    return clientes

def obtener_distritos():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM distritos")
    distritos = c.fetchall()
    conn.close()
    return distritos

def agregar_cliente(nombre, correo, telefono):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, correo, telefono) VALUES (?, ?, ?)", (nombre, correo, telefono))
    conn.commit()
    conn.close()

def agregar_distrito(nombre, provincia):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO distritos (nombre, provincia) VALUES (?, ?)", (nombre, provincia))
    conn.commit()
    conn.close()
