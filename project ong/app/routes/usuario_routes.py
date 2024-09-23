from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app import db
from app.models import Usuario
# Crear Blueprint para auth
bp = Blueprint('usuario', __name__)

# Registro de usuarios
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        telefono = request.form['telefono']
        cedula = request.form['cedula']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        rol = request.form['rol']  # admin, veterinario, empleado, usuario

        # Verificar si el correo ya existe
        if Usuario.query.filter_by(email=email).first():
            flash('El correo ya está registrado.')
            return redirect(url_for('usuario.register'))

        # Crear nuevo usuario
        new_user = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            cedula=cedula,
            direccion=direccion,
            ciudad=ciudad,
            rol=rol
        )
        new_user.set_password(password)

        # Guardar en la base de datos
        db.session.add(new_user)
        db.session.commit()

        flash('Te has registrado con éxito. Ahora puedes iniciar sesión.')
        return redirect(url_for('usuario.login'))

    return render_template('usuarios/registro.html')

# Login de usuarios
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Buscar usuario por email
        user = Usuario.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)

            # Redirigir según el rol del usuario
            if user.rol == 'admin':
                return redirect(url_for('main.baseadm'))  # Ejemplo de ruta para admin
            elif user.rol == 'veterinario':
                return redirect(url_for('main.basevete'))
            elif user.rol == 'empleado':
                return redirect(url_for('main.baseemple'))
            else:  # usuario
                return redirect(url_for('main.baseusu'))
        else:
            flash('Correo o contraseña incorrectos.')
            return redirect(url_for('usuario.login'))

    return render_template('usuarios/login.html')

# Logout
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.')
    return redirect(url_for('usuario.login'))
