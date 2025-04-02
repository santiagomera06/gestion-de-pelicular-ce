from flask import Flask
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['UPLOAD_FOLDER'] = './static/imagenes'

# Configuración de MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'GestionPeliculas',
    'host': 'localhost',
    'port': 27017
}

# Conexión directa con PyMongo para la colección de usuarios
client = MongoClient('localhost', 27017)
baseDatos = client['GestionPeliculas']
usuarios = baseDatos['Nuevos_usuarios']

# Inicializar MongoEngine
db = MongoEngine(app)

# Importar controladores
from controladores.usuarioController import *
from controladores.generoController import *
from controladores.peliculasController import *

if __name__ == '__main__':
    # Crear usuario admin por defecto si no existe
    if usuarios.count_documents({'username': 'admin'}) == 0:
        usuarios.insert_one({
            'username': 'admin',
            'password': 'admin123',
            'nombre': 'Administrador',
            'email': 'admin@example.com'
        })
    
    app.run(port=3000, host='0.0.0.0', debug=True)
