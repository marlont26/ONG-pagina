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

@bp.route('/donaciones')
def donaciones():
    return render_template('/vistasusuario/donaciones.html')

@bp.route('/baseadm')
def baseadm():
    return render_template('bases/baseadm.html')

@bp.route('/baseemple')
def baseemple():
    return render_template('empleados/index.html')

@bp.route('/basevete')
def basevete():
    return render_template('veterinarios1/index.html')

@bp.route('/')
def baseusu():    
    return render_template('bases/baseusu.html')


#Rutas para listado de usuarios segun su rol

@bp.route('/indexv')
def indexv():
    veterinarios = Usuario.query.filter_by(rol='veterinario').all()
    return render_template('/veterinarios1/indexv.html', usuarios=veterinarios)

@bp.route('/indexe')
def indexe():
    empleados = Usuario.query.filter_by(rol='empleado').all()
    return render_template('/empleados1/indexe.html', usuarios=empleados)

@bp.route('/indexu')
def indexu():
    usuarios = Usuario.query.filter_by(rol='usuario').all()
    return render_template('/usuarios/indexu.html', usuarios=usuarios)


