
from flask import render_template, request, redirect, session, flash, url_for
from functools import wraps  
from app import usuarios  
from app import app  
import pymongo  


# DECORADOR PARA RUTAS PROTEGIDAS

def login_required(f):
    """Decorador que verifica si el usuario ha iniciado sesión"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:  # Si no hay usuario en sesión
            flash('Debe iniciar sesión para acceder a esta página', 'danger')
            return redirect(url_for('iniciarSesion'))
        return f(*args, **kwargs)  # Si está autenticado, continua con la función original
    return decorated_function


# RUTA PRINCIPAL (PÁGINA DE INICIO)

@app.route("/")
def iniciar():
    """Muestra la página de inicio de sesión"""
    return render_template("sesion.html")


#  INICIAR SESIÓN

@app.route("/iniciarSesion", methods=['GET', 'POST'])
def iniciarSesion():
    """Controlador para el proceso de autenticación"""
    try:
        if request.method == "POST":
        
            username = request.form["txtUsername"]
            password = request.form["txtPassword"]
            
            usuario = usuarios.find_one({"username": username, "password": password})
            
            if usuario:  
                session['username'] = username 
                return redirect(url_for("listar_peliculas"))  
            else:
                flash("Credenciales no válidas. Verifique", "danger")
        return redirect("/")  
    
    except pymongo.errors.PyMongoError as error:
        flash(f"Error de base de datos: {str(error)}", "danger")
        return redirect("/")


# RUTA: REGISTRAR NUEVO USUARIO

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    """Controlador para registro de nuevos usuarios"""
    if request.method == "POST":
        try:
           
            username = request.form["txtUsername"]
            password = request.form["txtPassword"]
            nombre = request.form["txtNombre"]
            email = request.form["txtEmail"]
            
            
            if usuarios.find_one({"username": username}):
                flash("Este nombre de usuario ya está registrado", "warning")
                return render_template("registrar.html")
            
            # Crea nuevo usuario en MongoDB
            usuarios.insert_one({
                "username": username,
                "password": password,
                "nombre": nombre,
                "email": email
            })
            
            flash("Usuario registrado exitosamente. Ahora puede iniciar sesión.", "success")
            return redirect("/")  # Redirige a página de login
        
        except pymongo.errors.PyMongoError as error:
            flash(f"Error al registrar usuario: {str(error)}", "danger")
    
    # Muestra formulario de registro (para GET)
    return render_template("registrar.html")


# CERRAR SESIÓN

@app.route("/salir")
def salir():
    """Finaliza la sesión del usuario"""
    session.clear() 
    flash("Ha cerrado la sesión exitosamente", "info")
    return redirect("/")  