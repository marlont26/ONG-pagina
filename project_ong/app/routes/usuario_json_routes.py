from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from app.models.usuario import Usuario
from app.models.empleado import Empleado
from app import db

bp = Blueprint('usuariojson', __name__, url_prefix='/usuariosgod')

@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': usuario.id,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'email': usuario.email,
        'telefono': usuario.telefono,
        'cedula': usuario.cedula,
        'rol': usuario.rol
    } for usuario in usuarios]), 200

@bp.route('/addusuario', methods=['POST'])
def add_usuario():
    data = request.json
    usuario_existente = Usuario.query.filter_by(email=data['email']).first()
    if usuario_existente:
        return jsonify({'message': 'El correo electrónico ya está registrado'}), 400

    # Verificar contraseña por defecto según rol
    contrasenas_por_defecto = {
        'admin': 'admin123',
        'veterinario': 'vet123',
        'empleado': 'emp123'
    }
    
    if data['rol'] in contrasenas_por_defecto:
        if data['password'] != contrasenas_por_defecto[data['rol']]:
            return jsonify({'message': f'Contraseña incorrecta para el rol de {data["rol"]}'}), 400

    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        apellido=data['apellido'],
        email=data['email'],
        password=generate_password_hash(data['password']),
        telefono=data['telefono'],
        cedula=data['cedula'],
        rol=data['rol']
    )
    
    db.session.add(nuevo_usuario)
    db.session.flush()

    if data['rol'] == 'empleado':
        nuevo_empleado = Empleado(idEmple=nuevo_usuario.id)
        db.session.add(nuevo_empleado)

    db.session.commit()
    return jsonify({'message': 'Usuario creado exitosamente'}), 201

@bp.route('/editusuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.json
        usuario.nombre = data['nombre']
        usuario.apellido = data['apellido']
        usuario.email = data['email']
        usuario.telefono = data['telefono']
        usuario.cedula = data['cedula']
        usuario.rol = data['rol']
        if 'password' in data:
            usuario.password = generate_password_hash(data['password'])
        
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado exitosamente'})
    return jsonify({'message': 'Usuario no encontrado'}), 404

@bp.route('/deleteusuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        # Si es empleado, eliminar primero el registro de empleado
        if usuario.rol == 'empleado':
            empleado = Empleado.query.filter_by(idEmple=usuario.id).first()
            if empleado:
                db.session.delete(empleado)
        
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado exitosamente'})
    return jsonify({'message': 'Usuario no encontrado'}), 404