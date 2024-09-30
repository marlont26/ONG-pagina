from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import Perro, SolicitudAdopcion, Empleado  # Importa los modelos necesarios
from app import db

bp = Blueprint('administrador', __name__)

@bp.route('/admin')
@login_required
def index():
    return render_template('administrador/indexadmin.html')

@bp.route('/admin/salon')
@login_required
def salon():
    return render_template('administrador/salon.html')

@bp.route('/admin/school')
@login_required
def school():
    return render_template('administrador/school.html')

@bp.route('/admin/perros')
@login_required
def perros():
    page = request.args.get('page', 1, type=int)
    perros = Perro.query.paginate(page=page, per_page=10)
    return render_template('administrador/perrosadmin.html', perros=perros)

@bp.route('/admin/perros/table')
@login_required
def perros_table():
    page = request.args.get('page', 1, type=int)
    perros = Perro.query.paginate(page=page, per_page=10)
    return render_template('administrador/table.html', perros=perros)

@bp.route('/admin/editperro/<int:id>', methods=['GET', 'POST'])
@login_required
def editperrosadmin(id):
    perro = Perro.query.get_or_404(id)
    if request.method == 'POST':
        # Aquí va la lógica para actualizar el perro
        pass
    return render_template('administrador/editperrosadmin.html', perro=perro)

@bp.route('/admin/deleteperro/<int:id>')
@login_required
def deleteperrosadmin(id):
    perro = Perro.query.get_or_404(id)
    db.session.delete(perro)
    db.session.commit()
    flash('Perro eliminado exitosamente', 'success')
    return redirect(url_for('administrador.perros'))

# Añade más rutas según sea necesario para otras funcionalidades del administrador