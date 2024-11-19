from flask import Flask, render_template, string, secrets

# Instancia de Flask en la app
app = Flask(__name__)

# Funcion que genera la contraseña
def generar_contraseña():
    caracter = string.ascii_leters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracter)) for _ in range(longitud))
    return contraseña     

# Ruta de la raiz de la app
@app.route("/")
async def index():
    return render_template("index.html")

