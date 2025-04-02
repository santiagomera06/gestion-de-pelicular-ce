

from flask import request
from models.genero import Genero
from app import app

@app.route("/genero/", methods=['GET'])
def listGeneros():
    try:
        mensaje = None
        generos = Genero.objects()
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "generos": generos}

@app.route("/generos", methods=['POST'])
def addGenero():
    try:
        mensaje = None
        estado = False
        if request.method == "POST":
            datos = request.get_json(force=True)
            genero = Genero(**datos)
            genero.save()
            estado = True
            mensaje = "Género agregado correctamente"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}