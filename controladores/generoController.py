# Importaciones básicas
from flask import render_template, request, flash, redirect, url_for
from models.genero import Genero  
from app import app  
from mongoengine import DoesNotExist  


# 1. Ruta para listar todos los géneros

@app.route('/generos')
def listar_generos():
    """Obtiene y muestra todos los géneros ordenados por nombre"""
    generos = Genero.objects().order_by('nombre')
    return render_template('listarGeneros.html', generos=generos)


# 2. Ruta para agregar nuevo género 

@app.route('/generos/agregar', methods=['GET', 'POST'])
def agregar_genero():
    """Muestra formulario (GET) o procesa creación (POST)"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        try:
            Genero(nombre=nombre).save()
            flash('Género agregado', 'success')
            return redirect(url_for('listar_generos'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    return render_template('agregarGenero.html')


# 3. Ruta para editar género existente 

@app.route('/generos/editar/<id>', methods=['GET', 'POST'])
def editar_genero(id):
    """Muestra formulario con datos (GET) o guarda cambios (POST)"""
    try:
        genero = Genero.objects.get(id=id)
        if request.method == 'POST':
            genero.nombre = request.form.get('nombre')
            genero.save()
            flash('Género actualizado', 'success')
            return redirect(url_for('listar_generos'))
    except DoesNotExist:
        flash('Género no encontrado', 'danger')
    return render_template('editarGenero.html', genero=genero)


# 4. Ruta para eliminar género 

@app.route('/generos/eliminar/<id>')
def eliminar_genero(id):
    """Elimina un género específico"""
    try:
        genero = Genero.objects.get(id=id)
        genero.delete()
        flash('Género eliminado', 'success')
    except DoesNotExist:
        flash('Género no encontrado', 'danger')
    return redirect(url_for('listar_generos'))