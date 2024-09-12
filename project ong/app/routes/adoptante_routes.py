from flask import Blueprint, render_template, request
from app.models import Usuario

bp = Blueprint('adoptante', __name__)

@bp.route('/adoptantes', methods=['GET'])
def index():
    # Buscar todos los usuarios (adoptantes)
    search_query = request.args.get('search', '')  # Obtener el término de búsqueda
    if search_query:
        adoptantes = Usuario.query.filter(
            (Usuario.nombre.ilike(f'%{search_query}%')) |
            (Usuario.apellido.ilike(f'%{search_query}%')) |
            (Usuario.telefono.ilike(f'%{search_query}%')) |
            (Usuario.cedula.ilike(f'%{search_query}%')) |
            (Usuario.email.ilike(f'%{search_query}%'))
        ).all()
    else:
        adoptantes = Usuario.query.all()  # Obtiene todos los usuarios sin filtro de búsqueda

    return render_template('adoptantes/index.html', adoptantes=adoptantes)
