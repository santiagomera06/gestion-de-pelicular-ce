from app import app
from flask import request
from models.pelicula import Pelicula

@app.route("/pelicula/", methods=['GET'])
def listPelicula():
    try:
        mensaje = None
        peliculas = Pelicula.objects()
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "peliculas": peliculas}

@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje = None
        estado = False
        if request.method == "POST":
            datos = request.get_json(force=True)
            pelicula = Pelicula(**datos)
            pelicula.save()
            estado = True
            mensaje = "Película agregada correctamente"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}
