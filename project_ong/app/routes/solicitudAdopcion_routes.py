from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models.solicitudAdopcion import SolicitudAdopcion
from app.models.perro import Perro


from app import db

bp = Blueprint('solicitud_adopcion', __name__)

@bp.route('/solicitudesadopciones')
@login_required
def index():
    solicitudes = SolicitudAdopcion.query.all()
    return render_template('solicitudesadopciones/index.html', solicitudes=solicitudes)

@bp.route('/aceptar_solicitud/<int:id>', methods=['POST'])
@login_required
def aceptar_solicitud(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'aceptada'
    db.session.commit()
    flash('Solicitud de adopción aceptada exitosamente.', 'success')
    return redirect(url_for('solicitud_adopcion.index'))

@bp.route('/aprobar/<int:id>', methods=['POST'])
@login_required
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    
    if current_user.rol != 'empleado':
        flash('No tienes permiso para realizar esta acción.', 'danger')
        return redirect(url_for('solicitud_adopcion.index'))
    
    if solicitud.estado != 'Pendiente':
        flash('Esta solicitud ya ha sido procesada.', 'warning')
        return redirect(url_for('solicitud_adopcion.index'))
    
    try:
        solicitud.estado = 'Aprobada'
        solicitud.idEmpleado = current_user.id

        perro = Perro.query.get_or_404(solicitud.idPerro)
        perro.estado = 'Adoptado'

        db.session.add(solicitud)
        db.session.add(perro)
        db.session.commit()
        
        flash('Solicitud aprobada con éxito y el estado del perro ha sido actualizado a Adoptado.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Ocurrió un error al aprobar la solicitud: {str(e)}', 'danger')
        # Considera registrar el error para debugging
    
    return redirect(url_for('solicitud_adopcion.index'))

@bp.route('/rechazar/<int:id>', methods=['POST'])
@login_required
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    
    if current_user.rol != 'empleado':
        flash('No tienes permiso para realizar esta acción.', 'danger')
        return redirect(url_for('solicitud_adopcion.index'))
    
    if solicitud.estado != 'Pendiente':
        flash('Esta solicitud ya ha sido procesada.', 'warning')
        return redirect(url_for('solicitud_adopcion.index'))
    
    solicitud.estado = 'Rechazada'
    solicitud.idEmpleado = current_user.id

    perro = Perro.query.get_or_404(solicitud.idPerro)
    perro.estado = 'En Adopción'

    try:
        db.session.commit()
        flash('Solicitud rechazada con éxito.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Ocurrió un error al rechazar la solicitud.', 'danger')
        # Considera registrar el error para debugging
    
    return redirect(url_for('solicitud_adopcion.index'))