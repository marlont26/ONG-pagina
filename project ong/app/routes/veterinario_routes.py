from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Veterinario, Perro  # Asegúrate de importar Perro
from flask_login import login_required
from app import db
from werkzeug.utils import secure_filename  # Importar secure_filename
import os  # Importar os

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
    return render_template('veterinarios1/show.html', veterinario=veterinario)

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
        edad = request.form['edad']
        estado = request.form['estado']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        tamaño = request.form['tamaño']
        descripcion = request.form['descripcion']
        imagen = request.files.get('imagen')
        genero = request.form['genero']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = filename
        else:
            ruta_imagen = None

        nuevo_perro = Perro(
            nombre=nombre,
            raza=raza,
            estadoSalud=estado_salud,
            edad=edad,
            estado=estado,
            color=color,
            fechaIngreso=fechaIngreso,
            tamaño=tamaño,
            descripcion=descripcion,
            imagen=ruta_imagen,
            genero=genero
        )
        db.session.add(nuevo_perro)
        db.session.commit()

        # Redirigir a la lista de perros después de añadir
        return redirect(url_for('veterinario.perrosvete'))

    # Renderizar la plantilla para añadir un perro
    return render_template('veterinarios1/addperrosvete.html')  # Asegúrate de que este archivo exista

@bp.route('/edit_perro/<int:id>', methods=['GET', 'POST'])
@login_required  # Solo usuarios autenticados pueden acceder a esta ruta
def editperrosvete(id):
    perro = Perro.query.get_or_404(id)
    if request.method == 'POST':
        perro.nombre = request.form['nombre']
        perro.raza = request.form['raza']
        perro.estadoSalud = request.form['estadoSalud']
        perro.edad = request.form['edad']
        perro.estado = request.form['estado']
        perro.color = request.form['color']
        perro.fechaIngreso = request.form['fechaIngreso']
        perro.tamaño = request.form['tamaño']
        perro.descripcion = request.form['descripcion']
        imagen = request.files.get('imagen')
        perro.genero = request.form['genero']
        
        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            perro.imagen = filename
        
        db.session.commit()
        return redirect(url_for('veterinario.perrosvete'))
    
    return render_template('veterinarios1/editperrosvete.html', perro=perro)

# Eliminar funciones para agregar o eliminar veterinarios

@bp.route('/search_perros', methods=['GET'])
@login_required
def search_perros():
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    
    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=10)
    else:
        perros = Perro.query.paginate(page=page, per_page=10)
    
    return render_template('veterinarios1/table.html', perros=perros)
@bp.route('/deleteperrosvete/<int:id>', methods=['POST'])
@login_required
def deleteperrosvete(id):
    perro = Perro.query.get_or_404(id)
    db.session.delete(perro)
    db.session.commit()
    return redirect(url_for('veterinario.perrosvete'))
