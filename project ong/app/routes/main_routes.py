from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('/vistasusuario/about.html')

@bp.route('/baseadm')
def baseadm():
    return render_template('/bases/baseadm.html')  # Cambia el nombre del archivo según sea necesario

@bp.route('/baseusu')
def baseusu():
    return render_template('/bases/baseusu.html')  # Cambia el nombre del archivo según sea necesario
