from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Empleado, Cuidado, SolicitudAdopcion
from app import db

bp = Blueprint('empleado', __name__)

@bp.route('/empleados')
def index():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleados=empleados)

@bp.route('/add/empleados', methods=['GET', 'POST'])
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
    return render_template('empleados/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
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

@bp.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

@bp.route('/solicitudes')
def solicitudes():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('solicitudes/index.html', solicitudes=solicitudes)

@bp.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

@bp.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

@bp.route('/<int:id>/cuidados')
def cuidados(id):
    empleado = Empleado.query.get_or_404(id)
    return render_template('empleados/cuidados.html', empleado=empleado)

# Nueva ruta para mostrar los detalles de un empleado
@bp.route('/empleado/<int:id>', methods=['GET'])
def show(id):
    empleado = Empleado.query.get_or_404(id)
    return render_template('empleados/show.html', empleado=empleado)
