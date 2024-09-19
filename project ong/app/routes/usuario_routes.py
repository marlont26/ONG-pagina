from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import Usuario

bp = Blueprint('usuario', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Utiliza login_user para registrar al usuario
            login_user(user)

            # Redirige según el rol del usuario
            if user.rol == 'admin':
                return redirect(url_for('main.baseadm'))
            elif user.rol == 'veterinario':
                return redirect(url_for('main.basevete'))
            elif user.rol == 'empleado':
                return redirect(url_for('main.baseemple'))
            elif user.rol == 'cliente':
                return redirect(url_for('main.baseusu'))
        else:
            flash('Email o contraseña inválidos')

    return render_template('usuarios/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        password = request.form['password']
        cedula = request.form['cedula']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        rol = request.form.get('rol')  # Obtén el rol del formulario

        # Verificar si el correo ya existe
        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('El correo ya existe.', 'error')
            return redirect(url_for('usuario.register'))

        # Crear el usuario con el rol especificado
        user = Usuario(
            email=email,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            cedula=cedula,
            direccion=direccion,
            ciudad=ciudad,
            rol=rol
        )

        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')

        # Redirige según el rol del nuevo usuario
        if rol == 'admin':
            return redirect(url_for('main.baseadm'))  # Redirige a vista de administrador
        elif rol == 'veterinario':
            return redirect(url_for('main.basevete'))  # Redirige a vista de veterinario
        elif rol == 'empleado':
            return redirect(url_for('main.baseemple'))  # Redirige a vista de empleado
        else:
            return redirect(url_for('main.baseusu'))  # Redirige a vista de cliente

    return render_template('usuarios/registro.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))