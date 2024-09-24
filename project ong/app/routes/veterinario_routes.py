from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Veterinario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app import db

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios')
def index():
    veterinarios = Veterinario.query.all()
    return render_template('veterinarios1/index.html', veterinarios=veterinarios)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user =  Veterinario.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            
            # Redirigir dependiendo del rol del usuario
            if user.rol == 'admin':
                return redirect(url_for('main.baseadm'))
            elif user.rol == 'veterinario':
                return redirect(url_for('main.basevete'))
            elif user.rol == 'empleado':
                return redirect(url_for('main.baseemple'))
            else:
                return redirect(url_for('main.baseusu'))
        else:
            flash('Email o contraseña inválidos')

    return render_template('usuarios/login.html')


@bp.route('/add/veterinarios', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        email = request.form['email']
        password = request.form['password']
        rol = request.form.get('rol', 'veterinario')

        # Verificar si el correo ya existe
        user = Veterinario.query.filter_by(email=email).first()
        if user:
            flash('El correo ya existe.', 'error')
            return redirect(url_for('veterinario.add'))

        # Crear el usuario con el rol especificado
        user = Veterinario(
            email=email,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            cedula=cedula,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            rol=rol
        )

        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        login_user(user)
        
        if rol == 'veterinario':
            return redirect(url_for('main.basevete'))
        elif rol =='empleado':
            return redirect(url_for('main.baseemple'))
        else:
            flash('Email o contraseña inválidos')

        return redirect(url_for('veterinario.index'))
    
    return render_template('veterinarios/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    veterinario = Veterinario.query.get_or_404(id)

    if request.method == 'POST':
        veterinario.nombre = request.form['nombre']
        veterinario.apellido = request.form['apellido']
        veterinario.especialidad = request.form['especialidad']
        veterinario.telefono = request.form['telefono']
        veterinario.email = request.form['email']
        
        db.session.commit()
        
        return redirect(url_for('veterinario.index'))

    return render_template('veterinarios/edit.html', veterinario=veterinario)

@bp.route('/delete/<int:id>')
def delete(id):
    veterinario = Veterinario.query.get_or_404(id)
    
    db.session.delete(veterinario)
    db.session.commit()

    return redirect(url_for('veterinario.index'))

@bp.route('/show/<int:id>')
def show(id):
    veterinario = Veterinario.query.get_or_404(id)
    return render_template('veterinarios/show.html', veterinario=veterinario)

@bp.route('/perrosvete')
def perrosvete():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')

    # Filtrar perros basados en la consulta de búsqueda
    if search_query:
        perros = Perro.query.filter(
            Perro.nombre.ilike(f'%{search_query}%') |
            Perro.raza.ilike(f'%{search_query}%') |
            Perro.estadoSalud.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=10)
    else:
        perros = Perro.query.paginate(page=page, per_page=10)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('veterinarios1/table.html ', perros=perros)

    return render_template('veterinarios/perrosvete.html', perros=perros)
# Ruta para archivos estáticos con url_for (añadido)
@bp.route('/static-file')
def static_file():
    return render_template('vetrinarios1/index.html', static_url=url_for('templates', filename='veterinarios1/index.html'))
