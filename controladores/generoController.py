from flask import render_template, request, flash, redirect, url_for
from models.genero import Genero
from app import app
from mongoengine import DoesNotExist

@app.route('/generos')
def listar_generos():
    from controladores.usuarioController import login_required
    @login_required
    def inner():
        generos = Genero.objects().order_by('nombre')
        return render_template('listarGeneros.html', generos=generos)
    return inner()

@app.route('/generos/agregar', methods=['GET', 'POST'])
def agregar_genero():
    from controladores.usuarioController import login_required
    @login_required
    def inner():
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            try:
                Genero(nombre=nombre).save()
                flash('Género agregado correctamente', 'success')
                return redirect(url_for('listar_generos'))
            except Exception as e:
                flash(f'Error al agregar género: {str(e)}', 'danger')
        
        return render_template('agregarGenero.html')
    return inner()

@app.route('/generos/editar/<id>', methods=['GET', 'POST'])
def editar_genero(id):
    from controladores.usuarioController import login_required
    @login_required
    def inner():
        try:
            genero = Genero.objects.get(id=id)
            if request.method == 'POST':
                genero.nombre = request.form.get('nombre')
                genero.save()
                flash('Género actualizado correctamente', 'success')
                return redirect(url_for('listar_generos'))
        except DoesNotExist:
            flash('Género no encontrado', 'danger')
        except Exception as e:
            flash(f'Error al actualizar género: {str(e)}', 'danger')
        
        return render_template('editarGenero.html', genero=genero)
    return inner()

@app.route('/generos/eliminar/<id>')
def eliminar_genero(id):
    from controladores.usuarioController import login_required
    @login_required
    def inner():
        try:
            genero = Genero.objects.get(id=id)
            genero.delete()
            flash('Género eliminado correctamente', 'success')
        except DoesNotExist:
            flash('Género no encontrado', 'danger')
        except Exception as e:
            flash(f'Error al eliminar género: {str(e)}', 'danger')
        return redirect(url_for('listar_generos'))
    return inner()
