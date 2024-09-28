from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.usuario import Usuario
from app.models.empleado import Empleado

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect_based_on_role(current_user)
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.password, password):
            if usuario.rol == 'empleado':
                empleado = Empleado.query.filter_by(usuario_id=usuario.id).first()
                if empleado:
                    login_user(empleado)
                else:
                    flash('Error en la cuenta de empleado. Contacte al administrador.', 'danger')
                    return redirect(url_for('auth.login'))
            else:
                login_user(usuario)
            
            flash("Login exitoso!", "success")
            return redirect_based_on_role(usuario)
        
        flash('Credenciales inválidas. Por favor, intente de nuevo.', 'danger')

    return render_template("/usuarios/login.html")

def redirect_based_on_role(usuario):
    if usuario.rol == 'admin':
        return redirect(url_for('main.baseadm'))
    elif usuario.rol == 'empleado':
        return redirect(url_for('empleado.dashboard'))
    elif usuario.rol == 'veterinario':
        return redirect(url_for('veterinario.index'))
    else:
        return redirect(url_for('main.baseusu'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))