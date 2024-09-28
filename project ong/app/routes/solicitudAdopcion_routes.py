from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import SolicitudAdopcion, Empleado
from app import db

bp = Blueprint('solicitud_adopcion', __name__)

@bp.route('/solicitudesadopciones')
@login_required
def index():
    # Filtrar por estado si se proporciona, de lo contrario mostrar todas las solicitudes
    estado = request.args.get('estado', None)
    
    if estado:
        solicitudes = SolicitudAdopcion.query.filter_by(estado=estado).all()
    else:
        solicitudes = SolicitudAdopcion.query.all()
    
    return render_template('solicitudesadopciones/index.html', solicitudes=solicitudes)

@bp.route('/aprobar/<int:id>', methods=['POST'])
@login_required
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)

    # Verifica si el usuario actual es un empleado
    empleado = Empleado.query.filter_by(idEmple=current_user.id).first()
    if not empleado:
        flash('Empleado no encontrado. Por favor, verifica tu cuenta.', 'danger')
        return redirect(url_for('solicitud_adopcion.index'))

    # Asigna el ID del empleado autenticado y aprueba la solicitud
    solicitud.estado = 'Aprobada'
    solicitud.idEmpleado = empleado.idEmple
    db.session.commit()

    flash('Solicitud aprobada con éxito.', 'success')
    return redirect(url_for('solicitud_adopcion.index'))

@bp.route('/rechazar/<int:id>', methods=['POST'])
@login_required
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)

    # Verifica si el usuario actual es un empleado
    empleado = Empleado.query.filter_by(idEmple=current_user.id).first()
    if not empleado:
        flash('Empleado no encontrado. Por favor, verifica tu cuenta.', 'danger')
        return redirect(url_for('solicitud_adopcion.index'))

    # Asigna el ID del empleado autenticado y rechaza la solicitud
    solicitud.estado = 'Rechazada'
    solicitud.idEmpleado = empleado.idEmple
    db.session.commit()

    flash('Solicitud rechazada con éxito.', 'success')
    return redirect(url_for('solicitud_adopcion.index'))
