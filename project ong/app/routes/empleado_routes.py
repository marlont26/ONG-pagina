from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Empleado, Cuidado, SolicitudAdopcion, Perro
import os
from werkzeug.utils import secure_filename
from app import db

bp = Blueprint('empleado', __name__)

# Ruta para listar todos los empleados
@bp.route('/empleados')
def index():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleado=empleados)

# Ruta para agregar un nuevo empleado

# Ruta para eliminar un empleado
@bp.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

# Ruta para ver las solicitudes de adopción pendientes
@bp.route('/solicitudesadopcionesemple')
def solicitudesadopcionesemple():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('empleados/solicitudesadopcionesemple.html', solicitudes=solicitudes)

# Ruta para aprobar una solicitud de adopción
@bp.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudesadopcionesemple'))  # Corrección aquí

# Ruta para rechazar una solicitud de adopción
@bp.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudesadopcionesemple'))  # Corrección aquí

# Ruta para ver los cuidados de un empleado (perros asignados)
@bp.route('/<int:id>/cuidados')
def cuidados(id):
    empleado = Empleado.query.get_or_404(id)
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    return render_template('empleados/cuidados.html', empleado=empleado, cuidados=cuidados)

# Ruta para el panel de control del empleado (dashboard)
@bp.route('/empleado/<int:id>/dashboard')
def dashboard(id):
    empleado = Empleado.query.get_or_404(id)
    solicitudes_pendientes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    perros = Perro.query.all()  # Para gestionar perros
    return render_template('empleados/dashboard.html', empleado=empleado, solicitudes_pendientes=solicitudes_pendientes, cuidados=cuidados, perros=perros)

# Ruta para archivos estáticos con url_for (añadido)
@bp.route('/static-file')
def static_file():
    return render_template('empleados/index.html', static_url=url_for('templates', filename='empleados/index.html'))



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

@bp.route('/empleado/perrosemple_nuevo', methods=['GET', 'POST'])
def perrosemple_nuevo():
    if request.method == 'POST':
        # Lógica para agregar un perro
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estado = request.form['estado']
        estadoSalud = request.form['estadoSalud']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        descripcion = request.form['descripcion']

        new_perro = Perro(
            nombre=nombre,
            raza=raza,
            edad=edad,
            estado=estado,
            estadoSalud=estadoSalud,
            color=color,
            fechaIngreso=fechaIngreso,
            descripcion=descripcion,
        )
        db.session.add(new_perro)
        db.session.commit()

        return redirect(url_for('empleado.perrosemple'))  # Redirigir a la lista de perros
    return render_template('empleados/perrosemple.html')

@bp.route('/empleado/edit/<int:id>', methods=['GET', 'POST'])
def edit_perro(id):  # Manteniendo el nombre original
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
        perro.tamaño = request.form['tamaño']
        
        imagen = request.files.get('imagen')
        
        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            full_imagen_path = os.path.join(os.path.dirname(__file__), '..', imagen_path)
            
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(full_imagen_path), exist_ok=True)
            
            imagen.save(full_imagen_path)
            perro.imagen = filename

        db.session.commit()
        return redirect(url_for('empleado.perrosemple'))

    return render_template('empleados/editperrosemple.html', perro=perro)
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
        perro.tamaño = request.form['tamaño']  # Asegúrate de que este campo esté presente

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            perro.imagen = filename

        db.session.commit()
        return redirect(url_for('perro.perrosemple'))

    return render_template('empleados/editperrosemple.html', perro=perro)

@bp.route('/perros/count')
def count_perros():
    cantidad_perros = Perro.query.count()
    return {'cantidad_perros': cantidad_perros}

@bp.route('/deleteperrosemple/<int:id>')
def deleteperrosemple(id):
    perro = Perro.query.get_or_404(id)
    
    db.session.delete(perro)
    db.session.commit()

    return redirect(url_for('empleado.perrosemple'))
