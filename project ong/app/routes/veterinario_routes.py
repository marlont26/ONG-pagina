from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Veterinario, Perro  # Asegúrate de importar Perro
from flask_login import login_required
from app import db  # Añadir esta importación al principio del archivo

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios')
@login_required  # Asegúrate de que solo los usuarios autenticados accedan a esta ruta
def index():
    veterinarios = Veterinario.query.all()
    return render_template('veterinarios1/index.html', veterinarios=veterinarios)

@bp.route('/show/<int:id>')
@login_required  # Solo usuarios autenticados pueden ver detalles
def show(id):
    veterinario = Veterinario.query.get_or_404(id)
    return render_template('veterinarios/show.html', veterinario=veterinario)

@bp.route('/perrosvete')
@login_required  # Solo usuarios autenticados pueden acceder a esta ruta
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
        return render_template('veterinarios1/table.html', perros=perros)

    return render_template('veterinarios1/perrosvete.html', perros=perros)

@bp.route('/add_perro', methods=['GET', 'POST'])
@login_required  # Solo usuarios autenticados pueden acceder a esta ruta
def addperrosvete():
    if request.method == 'POST':
        # Lógica para agregar un nuevo perro
        nombre = request.form['nombre']
        raza = request.form['raza']
        estado_salud = request.form['estadoSalud']  # Asegúrate de que coincida con tu modelo
        # Agregar otros campos según sea necesario

        nuevo_perro = Perro(nombre=nombre, raza=raza, estadoSalud=estado_salud)
        # Guarda el nuevo perro en la base de datos
        # Recuerda añadir manejo de errores en producción
        db.session.add(nuevo_perro)
        db.session.commit()

        # Redirigir a la lista de perros después de añadir
        return redirect(url_for('veterinario.perrosvete'))

    # Renderizar la plantilla para añadir un perro
    return render_template('veterinarios1/add_perro.html')  # Asegúrate de que este archivo exista

# Eliminar funciones para agregar o eliminar veterinarios
