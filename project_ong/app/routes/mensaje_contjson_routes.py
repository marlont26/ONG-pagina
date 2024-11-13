from flask import Blueprint, render_template, request, jsonify
from app.models.mensaje_contacto import MensajeContacto
from app import db

bp = Blueprint('mensaje', __name__)

@bp.route('/mensaje', methods=['POST'])
def addmessage():
    data = request.json
    new_message = MensajeContacto(
        nombre=data ['nombre'],
        email=data['email'],
        mensaje=data['mensaje'],
        asunto=data['asunto']
    )

    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({'message': 'Message created successfully'}), 201

