from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Empleado, Cuidado, SolicitudAdopcion, Perro
from app import db

bp = Blueprint('empleado', __name__)

# Ruta para listar todos los empleados
@bp.route('/empleados')
def index():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleado=empleados)

# Ruta para agregar un nuevo empleado
@bp.route('/add/empleados', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        
        new_empleado = Empleado(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
        )
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('main.baseadm'))
    return render_template('empleados/add.html')

# Ruta para editar un empleado existente
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.apellido = request.form['apellido']
        empleado.email = request.form['email']
        empleado.telefono = request.form['telefono']
        
        db.session.commit()
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)

# Ruta para eliminar un empleado
@bp.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

# Ruta para ver las solicitudes de adopción pendientes
@bp.route('/solicitudes')
def solicitudes():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('solicitudes/index.html', solicitudes=solicitudes)

# Ruta para aprobar una solicitud de adopción
@bp.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

# Ruta para rechazar una solicitud de adopción
@bp.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

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
