from flask import request, jsonify
from models.pelicula import Pelicula
from models.genero import Genero
from app import app
from mongoengine.errors import DoesNotExist, ValidationError

@app.route("/pelicula/", methods=['GET'])
def list_peliculas():
    try:
        peliculas = Pelicula.objects()
        return jsonify([{
            "id": str(p.id),
            "codigo": p.codigo,
            "titulo": p.titulo,
            "protagonista": p.protagonista,
            "duracion": p.duracion,
            "resumen": p.resumen,
            "genero": {"id": str(p.genero.id), "nombre": p.genero.nombre},
            "foto": p.foto
        } for p in peliculas])
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/pelicula/", methods=['POST'])
def add_pelicula():
    try:
        datos = request.get_json()
        genero = Genero.objects.get(id=datos['genero']['id'])
        pelicula = Pelicula(
            codigo=datos['codigo'],
            titulo=datos['titulo'],
            protagonista=datos['protagonista'],
            duracion=datos['duracion'],
            resumen=datos['resumen'],
            genero=genero,
            foto=datos.get('foto', '')
        )
        pelicula.save()
        return jsonify({"estado": True, "mensaje": "Película agregada correctamente"})
    except DoesNotExist:
        return jsonify({"estado": False, "mensaje": "Género no encontrado"}), 404
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/pelicula/<id>", methods=['PUT'])
def update_pelicula(id):
    try:
        datos = request.get_json()
        pelicula = Pelicula.objects.get(id=id)
        genero = Genero.objects.get(id=datos['genero']['id'])
        pelicula.codigo = datos['codigo']
        pelicula.titulo = datos['titulo']
        pelicula.protagonista = datos['protagonista']
        pelicula.duracion = datos['duracion']
        pelicula.resumen = datos['resumen']
        pelicula.genero = genero
        pelicula.foto = datos.get('foto', pelicula.foto)
        pelicula.save()
        return jsonify({"estado": True, "mensaje": "Película actualizada correctamente"})
    except DoesNotExist:
        return jsonify({"estado": False, "mensaje": "Película o género no encontrado"}), 404
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500

@app.route("/pelicula/<id>", methods=['DELETE'])
def delete_pelicula(id):
    try:
        pelicula = Pelicula.objects.get(id=id)
        pelicula.delete()
        return jsonify({"estado": True, "mensaje": "Película eliminada correctamente"})
    except DoesNotExist:
        return jsonify({"estado": False, "mensaje": "Película no encontrada"}), 404
    except Exception as error:
        return jsonify({"estado": False, "mensaje": str(error)}), 500