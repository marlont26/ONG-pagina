from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.perro import Perro
from flask_login import login_required
from app import db
from werkzeug.utils import secure_filename
import os

bp = Blueprint('veterinario', __name__)

@bp.route('/perros', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def gestionar_perros():
    if request.method == 'GET':
        # Manejar búsqueda y listado
        page = request.args.get('page', 1, type=int)
        search_query = request.args.get('search', '')

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

        return render_template('veterinarios1/perros.html', perros=perros)

    elif request.method == 'POST':
        # Manejar adición de un nuevo perro
        data = request.form
        imagen = request.files.get('imagen')
        ruta_imagen = None
        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = filename

        nuevo_perro = Perro(
            nombre=data['nombre'],
            raza=data['raza'],
            estadoSalud=data['estadoSalud'],
            edad=data['edad'],
            estado=data['estado'],
            color=data['color'],
            fechaIngreso=data['fechaIngreso'],
            tamaño=data['tamaño'],
            descripcion=data['descripcion'],
            imagen=ruta_imagen,
            genero=data['genero']
        )
        db.session.add(nuevo_perro)
        db.session.commit()
        return redirect(url_for('veterinario.gestionar_perros'))

    elif request.method == 'PUT':
        # Manejar edición de un perro existente
        data = request.json
        perro = Perro.query.get_or_404(data['id'])
        perro.nombre = data.get('nombre', perro.nombre)
        perro.raza = data.get('raza', perro.raza)
        perro.estadoSalud = data.get('estadoSalud', perro.estadoSalud)
        perro.edad = data.get('edad', perro.edad)
        perro.estado = data.get('estado', perro.estado)
        perro.color = data.get('color', perro.color)
        perro.fechaIngreso = data.get('fechaIngreso', perro.fechaIngreso)
        perro.tamaño = data.get('tamaño', perro.tamaño)
        perro.descripcion = data.get('descripcion', perro.descripcion)
        perro.genero = data.get('genero', perro.genero)

        imagen = request.files.get('imagen')
        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            perro.imagen = filename

        db.session.commit()
        return jsonify({'success': True, 'message': 'Perro actualizado correctamente'})

    elif request.method == 'DELETE':
        # Manejar eliminación de un perro
        perro_id = request.json.get('id')
        perro = Perro.query.get_or_404(perro_id)
        db.session.delete(perro)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Perro eliminado correctamente'})
