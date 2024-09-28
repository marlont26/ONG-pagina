from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Perro, SolicitudAdopcion
from app import db

bp = Blueprint('vistasusuario', __name__)

@bp.route('/detalle/<int:perro_id>')
def detalle(perro_id):
    perro = Perro.query.get_or_404(perro_id)
    return render_template('vistasusuario/detalle.html', perro=perro)

@bp.route('/solicitar_adopcion/<int:perro_id>', methods=['POST'])
@login_required
def solicitar_adopcion(perro_id):
    if not current_user.is_authenticated:
        flash('Debes iniciar sesión para solicitar una adopción.', 'warning')
        return redirect(url_for('auth.login'))

    solicitud = SolicitudAdopcion(idAdoptante=current_user.id, idPerro=perro_id, estado='Pendiente')
    db.session.add(solicitud)
    db.session.commit()

    flash('¡Solicitud enviada con éxito!', 'success')
    return redirect(url_for('vistasusuario.detalle', perro_id=perro_id))
