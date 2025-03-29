from flask import Flask, render_template, request, redirect, url_for
from database import crear_base_datos, obtener_clientes, obtener_distritos, agregar_cliente, agregar_distrito

app = Flask(__name__)

# Crear base de datos al iniciar la aplicación
crear_base_datos()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['GET'])
def consulta():
    duda = request.args.get('consulta')
    
    # Aquí interpretamos la consulta. Si la consulta tiene que ver con criptomonedas, podemos buscarlo en la API.
    if "cripto" in duda.lower() or "precio" in duda.lower():
        # Lógica para consultar criptomonedas (no incluida aquí)
        return f"Tu consulta es sobre criptomonedas: {duda}"
    else:
        # Lógica para manejar otras consultas
        return f"Tu consulta es: {duda}. En este momento solo puedo mostrar precios de criptomonedas."

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
