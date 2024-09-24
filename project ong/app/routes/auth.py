from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models.usuario import Usuario

# Crear Blueprint para auth
auth_bp = Blueprint('auth', __name__)

# Login de usuarios
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Buscar usuario por email
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.password, password):
            login_user(usuario)
            flash("Login successful!", "success")
            
            # Redirigir según el rol del usuario
            if usuario.rol == 'admin':
                return redirect(url_for('main.baseadm'))
            elif usuario.rol == 'empleado':
                return redirect(url_for('empleado.index'))
            elif usuario.rol == 'veterinario':
                return redirect(url_for('veterinario.index'))
            else:  # rol usuario
                return redirect(url_for('main.baseusu'))
        
        flash('Invalid credentials. Please try again.', 'danger')

    if current_user.is_authenticated:
        if current_user.rol == 'admin':
            return redirect(url_for('main.baseadm'))
        elif current_user.rol == 'empleado':
            return redirect(url_for('empleado.index'))
        elif current_user.rol == 'veterinario':
            return redirect(url_for('veterinario.index'))
        else:
            return redirect(url_for('main.baseusu'))
    
    return render_template("/usuarios/login.html")

# Logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
