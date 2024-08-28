from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db

from app.models import Usuario, Rol  # Asegúrate de que Rol esté importado

bp = Blueprint('usuario', __name__)

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        tipo_usuario = request.form.get('tipo_usuario')

        if Usuario.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'danger')
            return redirect(url_for('usuario.registro'))

        nuevo_usuario = Usuario(
            nombre=nombre, 
            email=email, 
            rol=Rol[tipo_usuario]
        )
        nuevo_usuario.set_password(contrasena)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario registrado con éxito', 'success')
        return redirect(url_for('usuario.login'))

    return render_template('usuarios/registro.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(contrasena):
            login_user(usuario)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('home'))  # Ruta para la página principal
        else:
            flash('Email o contraseña incorrectos', 'danger')

    return render_template('usuarios/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('index'))

@bp.route('/perfil')
@login_required
def perfil():
    return render_template('usuarios/perfil.html', usuario=current_user)
