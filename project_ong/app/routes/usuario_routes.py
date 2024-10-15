from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models.usuario import Usuario
from app.models.empleado import Empleado
from app import db

# Crear el Blueprint para el usuario
bp = Blueprint('usuario', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        telefono = request.form['telefono']
        cedula = request.form['cedula']
        rol = request.form['rol']
        
        # Definir contraseñas por defecto para roles específicos
        contrasenas_por_defecto = {
            'admin': 'admin123',
            'veterinario': 'vet123',
            'empleado': 'emp123'
        }
        
        # Verificar la contraseña para roles específicos
        if rol in contrasenas_por_defecto:
            if password != contrasenas_por_defecto[rol]:
                flash(f'Contraseña incorrecta para el rol de {rol}. Por favor, use la contraseña por defecto.', 'danger')
                return redirect(url_for('usuario.register'))

        # Verificar si el correo ya está registrado
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('El correo electrónico ya está registrado. Intenta con otro.', 'danger')
            return redirect(url_for('usuario.register'))

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=generate_password_hash(password),  # Encriptar la contraseña
            telefono=telefono,
            cedula=cedula,
            rol=rol
        )
        
        # Guardar el nuevo usuario en la base de datos
        db.session.add(nuevo_usuario)
        db.session.flush()  # Esto asigna un ID al nuevo usuario

        # Si el rol es 'empleado', crear también una entrada en la tabla Empleado
        if rol == 'empleado':
            nuevo_empleado = Empleado(idEmple=nuevo_usuario.id)
            db.session.add(nuevo_empleado)

        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))  # Cambiado a auth.login
    
    # Renderizar el formulario de registro si es GET
    return render_template('/usuarios/registro.html')