from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Empleado, Cuidado, SolicitudAdopcion
from app import db

bp_empleado = Blueprint('empleado', __name__)

@bp_empleado.route('/')
def index():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleados=empleados)

@bp_empleado.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        puesto = request.form['puesto']
        
        new_empleado = Empleado(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            puesto=puesto
        )
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('empleado.index'))
    return render_template('empleados/create.html')

@bp_empleado.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.apellido = request.form['apellido']
        empleado.email = request.form['email']
        empleado.telefono = request.form['telefono']
        empleado.puesto = request.form['puesto']
        
        db.session.commit()
        
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)

@bp_empleado.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

@bp_empleado.route('/solicitudes')
def solicitudes():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('solicitudes/index.html', solicitudes=solicitudes)

@bp_empleado.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

@bp_empleado.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

@bp_empleado.route('/<int:id>/cuidados')
def cuidados(id):
    empleado = Empleado.query.get_or_404(id)
    return render_template('empleados/cuidados.html', empleado=empleado)
