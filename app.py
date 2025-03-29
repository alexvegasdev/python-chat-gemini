from flask import Flask, render_template, request
import sqlite3
import requests
import config  # Archivo de configuración con la API Key y base de datos

app = Flask(__name__)

# 📌 Función para obtener datos de SQLite
def obtener_datos():
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()

    # ✅ Traemos los clientes junto con su distrito
    cursor.execute("""
        SELECT clientes.nombre, clientes.correo, clientes.telefono, distritos.nombre 
        FROM clientes 
        JOIN distritos ON clientes.distrito_id = distritos.id
    """)
    clientes = cursor.fetchall()

    # ✅ Contamos cuántos clientes hay por distrito
    cursor.execute("""
        SELECT distritos.nombre, COUNT(clientes.id) AS total_clientes 
        FROM clientes 
        JOIN distritos ON clientes.distrito_id = distritos.id
        GROUP BY distritos.nombre
        ORDER BY total_clientes DESC
    """)
    distritos = cursor.fetchall()

    conn.close()
    return clientes, distritos

# 📌 Función para hacer la consulta a Gemini API
def consultar_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={config.API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        respuesta = response.json()
        # Extraer solo el texto de la respuesta
        if "candidates" in respuesta and respuesta["candidates"]:
            if "content" in respuesta["candidates"][0]:
                content = respuesta["candidates"][0]["content"]
                if "parts" in content and content["parts"]:
                    for part in content["parts"]:
                        if "text" in part:
                            return part["text"]  # Devuelve solo el texto
        return "No se pudo extraer una respuesta de texto"
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route('/consulta', methods=['GET'])
def consulta():
    duda = request.args.get('consulta', '').lower()

    # 📌 Obtener datos de la base de datos
    clientes, distritos = obtener_datos()

    # ✅ Formateamos los clientes con su distrito
    clientes_str = "\n".join([f"{c[0]} - {c[1]} - {c[2]} - {c[3]}" for c in clientes])

    # ✅ Mostramos cuántos clientes hay en cada distrito
    distritos_str = "\n".join([f"{d[0]}: {d[1]} clientes" for d in distritos])

    datos_completos = f"""
    Lista de clientes con su distrito:
    {clientes_str}

    Cantidad de clientes por distrito:
    {distritos_str}
    """

    # 📌 Crear el prompt para Gemini
    prompt = f"""
    Aquí tienes información de clientes y distritos. 
    Responde la siguiente pregunta de manera clara y directa:

    Pregunta: {duda}
    """

    # 📌 Enviar la consulta a Gemini
    respuesta = consultar_gemini(datos_completos + "\n\n" + prompt)

    return render_template('index.html', respuesta=respuesta)

if __name__ == '__main__':
    app.run(debug=True)
