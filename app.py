from flask import Flask, render_template, request, redirect, url_for
from database import crear_base_datos, obtener_clientes, obtener_distritos, agregar_cliente, agregar_distrito
import sqlite3
from config import DATABASE

app = Flask(__name__)

# Crear base de datos al iniciar la aplicación
crear_base_datos()

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar las consultas
@app.route('/consulta', methods=['GET'])
def consulta():
    duda = request.args.get('consulta', '').lower()

    # Variable para almacenar la respuesta
    respuesta = ""

    # Consultar por clientes
    if 'clientes' in duda:
        clientes = obtener_clientes()
        respuesta = '<ul>'
        for cliente in clientes:
            respuesta += f'<li>{cliente[1]} ({cliente[2]} - {cliente[3]})</li>'
        respuesta += '</ul>'
    
    # Consultar por distritos
    elif 'distritos' in duda:
        distritos = obtener_distritos()
        respuesta = '<ul>'
        for distrito in distritos:
            respuesta += f'<li>{distrito[1]}, {distrito[2]}</li>'
        respuesta += '</ul>'

    # Consultas relacionadas con criptomonedas
    elif 'cripto' in duda or 'precio' in duda:
        # Aquí puedes agregar tu lógica de consulta de criptomonedas
        respuesta = f"Tu consulta es sobre criptomonedas: {duda}"

    # Respuesta por defecto si no se puede entender la consulta
    else:
        respuesta = f"Tu consulta es: {duda}. En este momento solo puedo mostrar precios de criptomonedas, clientes o distritos."

    # Regresar la respuesta a la página de inicio (index.html)
    return render_template('index.html', respuesta=respuesta)

# Ruta para mostrar y agregar clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        agregar_cliente(nombre, correo, telefono)
        return redirect(url_for('clientes'))  # Redirige para evitar reenvíos de formulario

    clientes = obtener_clientes()
    return render_template('clientes.html', clientes=clientes)

# Ruta para mostrar y agregar distritos
@app.route('/distritos', methods=['GET', 'POST'])
def distritos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        provincia = request.form['provincia']
        agregar_distrito(nombre, provincia)
        return redirect(url_for('distritos'))  # Redirige para evitar reenvíos de formulario

    distritos = obtener_distritos()
    return render_template('distritos.html', distritos=distritos)

# Inicializa el servidor cuando el script se ejecute
if __name__ == '__main__':
    app.run(debug=True)
