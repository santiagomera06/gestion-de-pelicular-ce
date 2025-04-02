from flask import request, jsonify
from models.genero import Genero
from app import app
from mongoengine.errors import DoesNotExist, ValidationError, NotUniqueError

@app.route("/genero/", methods=['GET'])
def list_generos():
    try:
        generos = Genero.objects()
        return jsonify([{"id": str(g.id), "nombre": g.nombre} for g in generos])
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/genero/", methods=['POST'])
def add_genero():
    try:
        datos = request.get_json()
        genero = Genero(nombre=datos['nombre'])
        genero.save()
        return jsonify({"estado": True, "mensaje": "Género agregado correctamente"})
    except NotUniqueError:
        return jsonify({"estado": False, "mensaje": "Este género ya existe"}), 400
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/genero/<id>", methods=['PUT'])
def update_genero(id):
    try:
        datos = request.get_json()
        genero = Genero.objects.get(id=id)
        genero.nombre = datos['nombre']
        genero.save()
        return jsonify({"estado": True, "mensaje": "Género actualizado correctamente"})
    except DoesNotExist:
        return jsonify({"estado": False, "mensaje": "Género no encontrado"}), 404
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/genero/<id>", methods=['DELETE'])
def delete_genero(id):
    try:
        genero = Genero.objects.get(id=id)
        genero.delete()
        return jsonify({"estado": True, "mensaje": "Género eliminado correctamente"})
    except DoesNotExist:
        return jsonify({"estado": False, "mensaje": "Género no encontrado"}), 404
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500