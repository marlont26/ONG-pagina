from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Empleado, Cuidado, SolicitudAdopcion, Perro, MensajeContacto
import os
from werkzeug.utils import secure_filename
from app import db

bp = Blueprint('empleado', __name__)

@bp.route('/empleados')
def index():
    empleados = Empleado.query.all()
    mensajes = MensajeContacto.query.all()
    return render_template('empleados/index.html', empleado=empleados, mensajes=mensajes)

@bp.route('/add/empleados', methods=['GET', 'POST'])
@bp.route('/addemple', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        cedula = request.form['cedula']

        new_empleado = Empleado(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            password=password,
            cedula=cedula,
        )
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('main.baseadm'))
    return render_template('empleados1/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_empleado(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.apellido = request.form['apellido']
        empleado.email = request.form['email']
        empleado.telefono = request.form['telefono']
        empleado.password = request.form['password']
        empleado.cedula = request.form['cedula']
        
        db.session.commit()
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)

@bp.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    
    SolicitudAdopcion.query.filter_by(idAdoptante=empleado.id).delete()
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

@bp.route('/solicitudesadopcionesemple')
def solicitudesadopcionesemple():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    empleados = Empleado.query.all()
    return render_template('empleados/solicitudesadopcionesemple.html', solicitudes=solicitudes, empleados=empleados)

@bp.route('/aprobar/<int:id>', methods=['POST'])
@login_required
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)

    solicitud.estado = 'Aprobada'
    solicitud.idEmpleado = current_user.id

    perro = Perro.query.get_or_404(solicitud.idPerro)
    perro.estado = 'Adoptado'

    db.session.commit()

    flash('Solicitud aprobada con éxito.', 'success')
    return redirect(url_for('empleado.solicitudesadopcionesemple'))

@bp.route('/rechazar/<int:id>', methods=['POST'])
@login_required
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)

    solicitud.estado = 'Rechazada'
    solicitud.idEmpleado = current_user.id

    perro = Perro.query.get_or_404(solicitud.idPerro)
    perro.estado = 'En Adopción'

    db.session.commit()

    flash('Solicitud rechazada con éxito.', 'success')
    return redirect(url_for('empleado.solicitudesadopcionesemple'))

@bp.route('/<int:id>/cuidados')
def cuidados(id):
    empleado = Empleado.query.get_or_404(id)
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    return render_template('empleados/cuidados.html', empleado=empleado, cuidados=cuidados)

@bp.route('/empleado/<int:id>/dashboard')
def dashboard(id):
    empleado = Empleado.query.get_or_404(id)
    solicitudes_pendientes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    perros = Perro.query.all()
    return render_template('empleados/dashboard.html', empleado=empleado, solicitudes_pendientes=solicitudes_pendientes, cuidados=cuidados, perros=perros)

@bp.route('/static-file')
def static_file():
    return render_template('empleados/index.html', static_url=url_for('templates', filename='empleados/index.html'))

@bp.route('/perrosemple')
def perrosemple():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '')

    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=per_page)
    else:
        perros = Perro.query.paginate(page=page, per_page=per_page)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('empleados/table.html', perros=perros)

    return render_template('empleados/perrosemple.html', perros=perros)

@bp.route('/empleado/perrosemple_nuevo', methods=['GET', 'POST'])
def perrosemple_nuevo():
    if request.method == 'POST':
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

        return redirect(url_for('empleado.perrosemple'))
    return render_template('empleados/perrosemple.html')

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
        perro.tamaño = request.form['tamaño']

        imagen = request.files.get('imagen')
        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'img_perros', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            perro.imagen = filename

        db.session.commit()
        return redirect(url_for('empleado.perrosemple'))

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

@bp.route('/solicitudes/count')
def count_solicitudes():
    cantidad_solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').count()
    return {'cantidad_solicitudes': cantidad_solicitudes}