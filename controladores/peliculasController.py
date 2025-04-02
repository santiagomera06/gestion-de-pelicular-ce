
from flask import render_template, request, flash, redirect, url_for
from models.pelicula import Pelicula  
from models.genero import Genero      
from werkzeug.utils import secure_filename  
from app import app  
import os  
from mongoengine import DoesNotExist  

# Extensiones de imagen permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# FUNCIÓN AUXILIAR
def allowed_file(filename):
    """Valida que la extensión del archivo sea permitida"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# LISTADO DE PELÍCULAS

@app.route('/peliculas')
def listar_peliculas():
    """Controlador que muestra todas las películas ordenadas por título"""
    peliculas = Pelicula.objects().order_by('titulo')  # Consulta a MongoDB
    return render_template('listarPeliculas.html', peliculas=peliculas)

#  AGREGAR PELÍCULA (CREATE)
@app.route('/peliculas/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    """Controlador para agregar nuevas películas"""
    generos = Genero.objects().order_by('nombre')  
    if request.method == 'POST':
        try:
            
            datos = {
                'codigo': int(request.form.get('codigo')),
                'titulo': request.form.get('titulo'),
                'protagonista': request.form.get('protagonista'),
                'duracion': int(request.form.get('duracion')),
                'resumen': request.form.get('resumen'),
                'genero': Genero.objects.get(id=request.form.get('genero_id'))
            }
            
            # Procesamiento de la imagen (si se subió)
            if 'foto' in request.files:
                file = request.files['foto']
                if file.filename != '' and allowed_file(file.filename):
                    filename = secure_filename(file.filename) 
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    datos['foto'] = filename   
            # Crea  película
            Pelicula(**datos).save()
            flash('Película agregada correctamente', 'success')
            return redirect(url_for('listar_peliculas'))
            
        except Exception as e:
            flash(f'Error al agregar película: {str(e)}', 'danger')
    
    return render_template('agregarPelicula.html', generos=generos)


#  EDITAR PELÍCULA

@app.route('/peliculas/editar/<id>', methods=['GET', 'POST'])
def editar_pelicula(id):
    """Controlador para editar películas existentes"""
    try:
        pelicula = Pelicula.objects.get(id=id) 
        generos = Genero.objects().order_by('nombre')  
        
        if request.method == 'POST':
            pelicula.codigo = int(request.form.get('codigo'))
            pelicula.titulo = request.form.get('titulo')
            pelicula.protagonista = request.form.get('protagonista')
            pelicula.duracion = int(request.form.get('duracion'))
            pelicula.resumen = request.form.get('resumen')
            pelicula.genero = Genero.objects.get(id=request.form.get('genero_id'))
            
            # Procesamiento de la imagen (si se subió)
            if 'foto' in request.files:
                file = request.files['foto']
                if file.filename != '' and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    pelicula.foto = filename
            
            pelicula.save()  
            flash('Película actualizada correctamente', 'success')
            return redirect(url_for('listar_peliculas'))
            
    except DoesNotExist:
        flash('Película no encontrada', 'danger')
    
    return render_template('editarPelicula.html', pelicula=pelicula, generos=generos)


# ELIMINAR PELÍCULA 

@app.route('/peliculas/eliminar/<id>')
def eliminar_pelicula(id):
    """Controlador para eliminar películas"""
    try:
        pelicula = Pelicula.objects.get(id=id) 
        pelicula.delete()  
        flash('Película eliminada correctamente', 'success')
    except DoesNotExist:
        flash('Película no encontrada', 'danger')
    return redirect(url_for('listar_peliculas'))  