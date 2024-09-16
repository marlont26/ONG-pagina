from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Usuario # Asegúrate de que Rol esté importado

bp = Blueprint('usuario', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            
            # Redirigir dependiendo del rol del usuario
            if user.rol == 'admin':
                return redirect(url_for('main.baseadm'))  # Redirige a la vista de administrador
            else:
                return redirect(url_for('main.baseusu'))  # Redirige a la vista de usuario
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
        rol = request.form.get('rol', 'usuario')  # Obtener el rol del formulario, por defecto 'usuario'

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
            cedula=cedula,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            rol=rol
        )

        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        login_user(user)
        
        if rol == 'admin':
            return redirect(url_for('main.baseadm'))  # Redirige a la vista de administrador
        else:
            return redirect(url_for('main.baseusu'))  # Redirige a la vista de usuario

    return render_template('usuarios/registro.html')



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))
