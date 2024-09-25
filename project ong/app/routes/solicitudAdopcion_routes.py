from flask import Blueprint, render_template, request, redirect, url_for
from app.models import SolicitudAdopcion, Empleado
from app import db

bp = Blueprint('solicitud_adopcion', __name__)

@bp.route('/solicitudesadopciones')
def index():
    solicitudes = SolicitudAdopcion.query.all()
    return render_template('solicitudesadopciones/index.html', solicitudes=solicitudes)

@bp.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    solicitud.idEmpleado = 1  # Debes cambiar esto por el ID del empleado real que aprueba la solicitud
    db.session.commit()
    return redirect(url_for('solicitud_adopcion.index'))

@bp.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    solicitud.idEmpleado = 1  # Debes cambiar esto por el ID del empleado real que rechaza la solicitud
    db.session.commit()
    return redirect(url_for('solicitud_adopcion.index'))

@bp.route('/solicitudesadopcionesemple')
def solicitudesadopcionesemple():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('empleados/solicitudesadopcionesemple.html', solicitudes=solicitudes)

