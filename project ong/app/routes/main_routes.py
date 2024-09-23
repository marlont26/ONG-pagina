from flask import Blueprint, render_template
from flask_login import login_required
from app.models.usuario import Usuario

bp = Blueprint('main', __name__)

@bp.route('/about')
def about():
    return render_template('/vistasusuario/about.html')

@bp.route('/contacto')
def contacts():
    return render_template('/vistasusuario/contacts.html')

@bp.route('/perros_adopcion')
@login_required
def usuperro():
    return render_template('/vistasusuario/perros.html')

@bp.route('/baseadm')
@login_required
def baseadm():
    return render_template('bases/baseadm.html')

@bp.route('/baseemple')
@login_required
def baseemple():
    return render_template('bases/baseemple.html')

@bp.route('/basevete')
@login_required
def basevete():
    return render_template('bases/basevete.html')

@bp.route('/baseusu')
@login_required
def baseusu():    
    return render_template('bases/baseusu.html')
