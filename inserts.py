import sqlite3
from config import DATABASE

def insertar_datos():
    """Inserta datos de prueba en la base de datos."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Insertar distritos si no existen
    distritos = [
        ("Miraflores", "Lima"),
        ("San Isidro", "Lima"),
        ("Barranco", "Lima"),
        ("Surco", "Lima"),
        ("La Molina", "Lima")
    ]
    c.executemany("INSERT INTO distritos (nombre, provincia) VALUES (?, ?)", distritos)

    # Obtener IDs de los distritos insertados
    c.execute("SELECT id FROM distritos")
    distrito_ids = [row[0] for row in c.fetchall()]

    # Insertar 40 clientes con referencia a distritos
    clientes = [
        ("Juan Pérez", "juan@example.com", "987654321", distrito_ids[0]),
        ("Ana Gómez", "ana@example.com", "987654322", distrito_ids[1]),
        ("Carlos Torres", "carlos@example.com", "987654323", distrito_ids[0]),
        ("María López", "maria@example.com", "987654324", distrito_ids[0]),
        ("Pedro Ramírez", "pedro@example.com", "987654325", distrito_ids[4]),
        
        # Más clientes agregados
        ("Lucía Fernández", "lucia@example.com", "987654326", distrito_ids[0]),
        ("Raúl Castillo", "raul@example.com", "987654327", distrito_ids[1]),
        ("Fernanda Vega", "fernanda@example.com", "987654328", distrito_ids[2]),
        ("Eduardo Herrera", "eduardo@example.com", "987654329", distrito_ids[3]),
        ("Gabriela Ruiz", "gabriela@example.com", "987654330", distrito_ids[4]),
        
        ("José Paredes", "jose@example.com", "987654331", distrito_ids[0]),
        ("Mónica Salazar", "monica@example.com", "987654332", distrito_ids[1]),
        ("Ricardo Soto", "ricardo@example.com", "987654333", distrito_ids[2]),
        ("Elena Bravo", "elena@example.com", "987654334", distrito_ids[3]),
        ("Santiago Rivas", "santiago@example.com", "987654335", distrito_ids[4]),
        
        ("Paola Ramírez", "paola@example.com", "987654336", distrito_ids[0]),
        ("Tomás Morales", "tomas@example.com", "987654337", distrito_ids[1]),
        ("Daniela Peña", "daniela@example.com", "987654338", distrito_ids[2]),
        ("Hugo Vargas", "hugo@example.com", "987654339", distrito_ids[3]),
        ("Valeria Campos", "valeria@example.com", "987654340", distrito_ids[4]),
        
        ("Rodrigo Silva", "rodrigo@example.com", "987654341", distrito_ids[0]),
        ("Estefanía León", "estefania@example.com", "987654342", distrito_ids[1]),
        ("David Guzmán", "david@example.com", "987654343", distrito_ids[2]),
        ("Camila Cáceres", "camila@example.com", "987654344", distrito_ids[3]),
        ("Mateo Navarro", "mateo@example.com", "987654345", distrito_ids[4]),
        
        ("Luis Mendoza", "luis@example.com", "987654346", distrito_ids[0]),
        ("Fabiola Torres", "fabiola@example.com", "987654347", distrito_ids[0]),
        ("Alberto Estrada", "alberto@example.com", "987654348", distrito_ids[0]),
        ("Carolina Ponce", "carolina@example.com", "987654349", distrito_ids[0]),
        ("Emilio Acosta", "emilio@example.com", "987654350", distrito_ids[0]),
        
        ("Natalia Rojas", "natalia@example.com", "987654351", distrito_ids[0]),
        ("Felipe Orellana", "felipe@example.com", "987654352", distrito_ids[1]),
        ("Ximena Calderón", "ximena@example.com", "987654353", distrito_ids[2]),
        ("Sebastián Núñez", "sebastian@example.com", "987654354", distrito_ids[3]),
        ("Patricia Arce", "patricia@example.com", "987654355", distrito_ids[4])
    ]
    c.executemany("INSERT INTO clientes (nombre, correo, telefono, distrito_id) VALUES (?, ?, ?, ?)", clientes)

    conn.commit()
    conn.close()
    print("✅ 40 clientes insertados correctamente.")

# Ejecutar la función de inserción
if __name__ == "__main__":
    insertar_datos()
