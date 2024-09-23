from flask import Blueprint, render_template, request, flash, url_for, redirect

from app.models import MensajeContacto
from app import db

bp = Blueprint('mensaje', __name__)

@bp.route('/mensajes', methods=['GET', 'POST'])
def addmensaje():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']


        newMensaje = MensajeContacto (nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
        db.session.add(newMensaje)
        db.session.commit()


    return render_template('vistasusuario/contacts.html')