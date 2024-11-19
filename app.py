from flask import Flask, render_template, request
import string 
import secrets

# Instancia de Flask en la app
app = Flask(__name__)

# Funcion que genera la contraseña
def generar_contraseña(longitud=12):
    caracter = string.ascii_leters + string.digits + string.puntuation
    contraseña = ''.join(secrets.choice(caracter) for _ in range(longitud))
    return contraseña     

# Ruta de la raiz de la app
@app.route("/")
async def index():
    return render_template("index.html")

# Ruta generar contraseña
@app.route("/generar", methods={"POST"})
async def generar():
    longitud = int(request.form.get('longitud', 12))
    contraseña = generar_contraseña('longitud')
    return render_template('result.html', contraseña=contraseña)
