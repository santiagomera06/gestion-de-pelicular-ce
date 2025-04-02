from flask import render_template, request, redirect, session, flash, url_for
from functools import wraps
from app import usuarios
from app import app
import pymongo

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debe iniciar sesión para acceder a esta página', 'danger')
            return redirect(url_for('iniciarSesion'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def iniciar():
    return render_template("sesion.html")

@app.route("/iniciarSesion", methods=['GET', 'POST'])
def iniciarSesion():
    try:
        if request.method == "POST":
            username = request.form["txtUsername"]
            password = request.form["txtPassword"]
            
            usuario = usuarios.find_one({"username": username, "password": password})
            
            if usuario:
                session['username'] = username
                session['user_id'] = str(usuario['_id'])
                return redirect(url_for("listar_peliculas"))
            else:
                flash("Credenciales no válidas. Verifique", "danger")
                return redirect("/")
        else:
            flash("Debe ingresar sus credenciales desde el formulario", "warning")
            return redirect("/")
    except pymongo.errors.PyMongoError as error:
        flash(f"Error de base de datos: {str(error)}", "danger")
        return redirect("/")

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == "POST":
        try:
            username = request.form["txtUsername"]
            password = request.form["txtPassword"]
            nombre = request.form["txtNombre"]
            email = request.form["txtEmail"]
            
            if usuarios.find_one({"username": username}):
                flash("Este nombre de usuario ya está registrado", "warning")
                return render_template("registrar.html")
            
            usuarios.insert_one({
                "username": username,
                "password": password,
                "nombre": nombre,
                "email": email
            })
            
            flash("Usuario registrado exitosamente. Ahora puede iniciar sesión.", "success")
            return redirect("/")
        except pymongo.errors.PyMongoError as error:
            flash(f"Error al registrar usuario: {str(error)}", "danger")
    
    return render_template("registrar.html")

@app.route("/salir")
def salir():
    session.clear()
    flash("Ha cerrado la sesión exitosamente", "info")
    return redirect("/")
