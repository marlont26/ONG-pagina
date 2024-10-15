from flask import Blueprint, render_template, request, jsonify
from app.models.mensaje_contacto import MensajeContacto
from app import db

bp = Blueprint('mensaje', __name__)

@bp.route('/mensajes', methods=['POST'])
def addmensaje():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        newMensaje = MensajeContacto(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
        db.session.add(newMensaje)
        db.session.commit()
        
        return jsonify(success=True)

    return jsonify(success=False, error="Invalid request method")