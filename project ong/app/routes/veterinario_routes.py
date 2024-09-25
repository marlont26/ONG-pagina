from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Veterinario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app import db

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios')
def index():
    veterinarios = Veterinario.query.all()
    return render_template('veterinarios1/index.html', veterinarios=veterinarios)

@bp.route('/delete/<int:id>')
def delete(id):
    veterinario = Veterinario.query.get_or_404(id)
    
    db.session.delete(veterinario)
    db.session.commit()

    return redirect(url_for('veterinario.index'))

@bp.route('/show/<int:id>')
def show(id):
    veterinario = Veterinario.query.get_or_404(id)
    return render_template('veterinarios/show.html', veterinario=veterinario)

@bp.route('/perrosvete')
def perrosvete():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')

    # Filtrar perros basados en la consulta de búsqueda
    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=10)
    else:
        perros = Perro.query.paginate(page=page, per_page=10)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('veterinarios1/table.html ', perros=perros)

    return render_template('veterinarios/perrosvete.html', perros=perros)
# Ruta para archivos estáticos con url_for (añadido)
@bp.route('/static-file')
def static_file():
    return render_template('vetrinarios1/index.html', static_url=url_for('templates', filename='veterinarios1/index.html'))
