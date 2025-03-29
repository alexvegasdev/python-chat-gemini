from flask import Flask, render_template, request
import requests
from config import API_KEY  # Asegúrate de que este archivo tenga tu clave de API
from database import crear_base_datos, obtener_clientes, agregar_cliente

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Crear base de datos al iniciar la aplicación
crear_base_datos()

# Función para obtener el precio de una criptomoneda usando la API de Gemini
def obtener_precio_cripto(symbol="BTCUSD"):
    url = f"https://api.gemini.com/v1/pubticker/{symbol}"
    headers = {
        "Content-Type": "application/json",
        "X-GEMINI-APIKEY": API_KEY  # Asegúrate de que la clave esté correctamente configurada
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'last' in data:
        return data['last']  # Último precio
    return None

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    clientes = obtener_clientes()
    return render_template('clientes.html', clientes=clientes)

@app.route('/precio_cripto', methods=['GET'])
def precio_cripto():
    symbol = request.args.get('symbol', 'BTCUSD')
    precio = obtener_precio_cripto(symbol)
    if precio:
        return f"El precio actual de {symbol} es: ${precio}"
    else:
        return f"No se pudo obtener el precio de {symbol}"

@app.route('/agregar_cliente', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    agregar_cliente(nombre, correo, telefono)
    return "Cliente agregado con éxito"

# Inicializa el servidor cuando el script se ejecute
if __name__ == '__main__':
    app.run(debug=True)
