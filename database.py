import sqlite3
from config import DATABASE

def crear_base_datos():
    """Crea la base de datos con las tablas necesarias."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Crear tabla de distritos
    c.execute('''
    CREATE TABLE IF NOT EXISTS distritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        provincia TEXT NOT NULL
    )
    ''')

    # Crear tabla de clientes con relación a distritos
    c.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        telefono TEXT NOT NULL,
        distrito_id INTEGER,
        FOREIGN KEY (distrito_id) REFERENCES distritos(id)
    )
    ''')

    conn.commit()
    conn.close()

def obtener_clientes():
    """Obtiene la lista de clientes con su distrito asociado."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
    SELECT clientes.id, clientes.nombre, clientes.correo, clientes.telefono, distritos.nombre AS distrito 
    FROM clientes
    LEFT JOIN distritos ON clientes.distrito_id = distritos.id
    """)
    clientes = c.fetchall()
    conn.close()
    return clientes

def obtener_distritos():
    """Obtiene la lista de distritos."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM distritos")
    distritos = c.fetchall()
    conn.close()
    return distritos

def agregar_cliente(nombre, correo, telefono, distrito_id):
    """Agrega un cliente con un distrito asociado."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, correo, telefono, distrito_id) VALUES (?, ?, ?, ?)", 
              (nombre, correo, telefono, distrito_id))
    conn.commit()
    conn.close()

def agregar_distrito(nombre, provincia):
    """Agrega un distrito."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO distritos (nombre, provincia) VALUES (?, ?)", (nombre, provincia))
    conn.commit()
    conn.close()

def obtener_datos():
    """Obtiene la lista de clientes junto con el nombre del distrito."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Consulta mejorada para obtener el nombre del distrito junto con los clientes
    c.execute("""
        SELECT clientes.nombre, clientes.correo, clientes.telefono, distritos.nombre 
        FROM clientes 
        JOIN distritos ON clientes.distrito_id = distritos.id
    """)
    clientes = c.fetchall()

    c.execute("SELECT id, nombre FROM distritos")
    distritos = c.fetchall()

    conn.close()
    return clientes, distritos

