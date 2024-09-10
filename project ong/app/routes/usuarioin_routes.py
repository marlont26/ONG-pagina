from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import login_required, current_user, login_user, logout_user
from app.models.usuarioin import Usuarioin

bp = Blueprint('usuarioin', __name__)

@bp.route('/usuarios', methods=['GET'])
def index():
    usuarios = Usuarioin.query.all()
    return render_template('usuariosin.html', usuarios=usuarios)

@bp.route('/usuariosadd', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrein = request.form['nombrein']
        emailin = request.form['emailin']
        passwordin = request.form['passwordin']

        user = Usuarioin(
            emailin = emailin,
            nombrein = nombrein,
            passwordin = generate_password_hash(passwordin, method='pbkdf2:sha256')
        )

        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        login_user(user)
        return redirect(url_for('main.home'))

    return render_template('usuariosin/index.html')


# Actualizar un usuario existente
@bp.route('/usuarios/<int:iduserin>', methods=['POST'])
def edit (iduserin):
    usuario = Usuarioin.query.get(iduserin)
    if not usuario:
        return "Usuario no encontrado.", 404
    
    nombrein = request.form.get('nombrein')
    emailin = request.form.get('emailin')
    passwordin = request.form.get('passwordin')

    usuario.nombrein = nombrein if nombrein else usuario.nombrein
    usuario.emailin = emailin if emailin else usuario.emailin
    usuario.adminin = bool(request.form.get('adminin', usuario.adminin))
    usuario.veterinarioin = bool(request.form.get('veterinarioin', usuario.veterinarioin))
    usuario.empleadoin = bool(request.form.get('empleadoin', usuario.empleadoin))

    if passwordin:
        usuario.set_password(passwordin)

    db.session.commit()

    return redirect(url_for('usuarios.obtener_usuarios'))

# Eliminar un usuario
@bp.route('/usuarios/eliminar/<int:iduserin>', methods=['GET'])
def delete(iduserin):
    usuario = Usuarioin.query.get(iduserin)
    if not usuario:
        return "Usuario no encontrado.", 404

    db.session.delete(usuario)
    db.session.commit()

    return redirect(url_for('usuarios.obtener_usuarios'))

# Verificar credenciales (login)
@bp.route('/usuarios/loginin', methods=['POST'])
def loginin():
    emailin = request.form.get('emailin')
    passwordin = request.form.get('passwordin')
    
    if not emailin or not passwordin:
        return "Datos insuficientes.", 400

    usuario = Usuarioin.query.filter_by(emailin=emailin).first()

    if usuario and usuario.check_password(passwordin):
        # Aquí puedes redirigir a una página de dashboard o similar
        return f"Bienvenido {usuario.nombrein}"
    else:
        return "Credenciales incorrectas.", 401