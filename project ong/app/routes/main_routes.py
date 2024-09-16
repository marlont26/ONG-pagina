from flask import Blueprint, render_template
from flask_login import login_required



bp = Blueprint('main', __name__)

@bp.route('/about')
def about():
    return render_template('/vistasusuario/about.html')

@bp.route('/admin')
@login_required
def baseadm():
    return render_template('bases/baseadm.html')

@bp.route('/baseemple')
def baseemple():
    return render_template('bases/baseemple.html')

@bp.route('/basevete')
def basevete():
    return render_template('bases/basevete.html')

@bp.route('/')
def baseusu():
    return render_template('bases/baseusu.html')
