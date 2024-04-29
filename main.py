from flask import Flask
from flask_cors import CORS
from backend.api.routes import api

#Config
app = Flask(__name__, static_folder='./frontend/dist') #Para cargar los archivos estaticos generados por Vue
app.config.from_object('config')
CORS(app, resources={r"/*":{'origins':'*'}})


# This code is for Flask run de Vue project
@app.route('/')
def index():
    return app.send_static_file('index.html')
@app.route('/<path:filename>')
def send_static(filename):
    return app.send_static_file(filename)


# Registrar el blueprint
app.register_blueprint(api)

if __name__ == "__main__":
    app.run()
