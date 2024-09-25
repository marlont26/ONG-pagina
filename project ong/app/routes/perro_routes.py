from flask import Blueprint, render_template, request, redirect, url_for
from app.models.perro import Perro
from app import db
from werkzeug.utils import secure_filename
import os

bp = Blueprint('perro', __name__)

@bp.route('/perros')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Fijar la cantidad de perros por página a 5
    search_query = request.args.get('search', '')

    # Filtrar perros basados en la consulta de búsqueda
    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=per_page)  # Usar per_page
    else:
        perros = Perro.query.paginate(page=page, per_page=per_page)  # Usar per_page

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('perros/table.html', perros=perros)

    return render_template('/vistasusuario/perros.html', perros=perros)

@bp.route('/add/perro', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estado = request.form['estado']
        estadoSalud = request.form['estadoSalud']
        tamaño = request.form['tamaño']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        descripcion = request.form['descripcion']
        imagen = request.files.get('imagen')

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = imagen_path

        else:
            ruta_imagen = None
        
        new_perro = Perro( 
            nombre=nombre,
            raza=raza,
            edad=edad,
            estadoSalud=estadoSalud,
            fechaIngreso=fechaIngreso,
            descripcion=descripcion,
            estado=estado,
            color=color,
            imagen=ruta_imagen,  # Corrección aquí
            tamaño=tamaño
        )
        db.session.add(new_perro)
        db.session.commit()
        
        return redirect(url_for('empleado.perrosemple'))  # Corrección aquí
    return render_template('perros/add.html')

@bp.route('/editperro/<int:id>', methods=['GET', 'POST'])
def edit(id):
    perro = Perro.query.get_or_404(id)

    if request.method == 'POST':
        perro.nombre = request.form['nombre']
        perro.raza = request.form['raza']
        perro.edad = request.form['edad']
        perro.estadoSalud = request.form['estadoSalud']
        perro.estado = request.form['estado']
        perro.color = request.form['color']
        perro.fechaIngreso = request.form['fechaIngreso']
        perro.descripcion = request.form['descripcion']
        
        db.session.commit()
        return redirect(url_for('perro.index'))

    return render_template('perros/edit.html', perro=perro)

@bp.route('/deleteperro/<int:id>')
def delete(id):
    perro = Perro.query.get_or_404(id)
    
    db.session.delete(perro)
    db.session.commit()

    return redirect(url_for('perro.index'))

@bp.route('/showperro/<int:id>')
def show(id):
    perro = Perro.query.get_or_404(id)
    return render_template('perros/show.html', perro=perro)


@bp.route('/perrosemple')
def perrosemple():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Fijar la cantidad de perros por página a 5
    search_query = request.args.get('search', '')

    # Filtrar perros basados en la consulta de búsqueda
    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=per_page)  # Usar per_page
    else:
        perros = Perro.query.paginate(page=page, per_page=per_page)  # Usar per_page

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('empleados/table.html', perros=perros)

    return render_template('empleados/perrosemple.html', perros=perros)
    # End Generation Here

@bp.route('/addperrosemple', methods=['GET', 'POST'])
def addperrosemple():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estado = request.form['estado']
        estadoSalud = request.form['estadoSalud']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        descripcion = request.form['descripcion']
        imagen = request.files.get('imagen')
        tamaño = request.form['tamaño']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = filename  # Corrección aquí
        else:
            ruta_imagen = None  # Corrección aquí

        new_perro = Perro(
            nombre=nombre,
            raza=raza,
            edad=edad,
            estadoSalud=estadoSalud,
            fechaIngreso=fechaIngreso,
            descripcion=descripcion,
            estado=estado,
            color=color,
            imagen=ruta_imagen,  # Corrección aquí
            tamaño=tamaño
        )
        db.session.add(new_perro)
        db.session.commit()

        return redirect(url_for('perro.perrosemple'))  # Corrección aquí
    return render_template('empleados/addperrosemple.html')

@bp.route('/editperrosemple/<int:id>', methods=['GET', 'POST'])
def editperrosemple(id):
    perro = Perro.query.get_or_404(id)
    if request.method == 'POST':
        perro.nombre = request.form['nombre']
        perro.raza = request.form['raza']
        perro.edad = request.form['edad']
        perro.estado = request.form['estado']
        perro.estadoSalud = request.form['estadoSalud']
        perro.color = request.form['color']
        perro.fechaIngreso = request.form['fechaIngreso']
        perro.descripcion = request.form['descripcion']
        imagen = request.files.get('imagen')
        perro.tamaño = request.form['tamaño']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            perro.imagen = filename

        db.session.commit()
        return redirect(url_for('perro.perrosemple'))

    return render_template('empleados/editperrosemple.html', perro=perro)




@bp.route('/deleteperrosemple/<int:id>')
def deleteperrosemple(id):
    perro = Perro.query.get_or_404(id)
    
    db.session.delete(perro)
    db.session.commit()

    return redirect(url_for('perro.perrosemple'))

