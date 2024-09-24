from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Empleado, Cuidado, SolicitudAdopcion, Perro
from app import db

bp = Blueprint('empleado', __name__)

# Ruta para listar todos los empleados
@bp.route('/empleados')
def index():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleado=empleados)

# Ruta para agregar un nuevo empleado   
@bp.route('/add/empleados', methods=['GET', 'POST'])
# Ruta para agregar un nuevo empleado
@bp.route('/addemple', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        cedula = request.form['cedula']

        
        new_empleado = Empleado(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            password=password,
            cedula=cedula,
        )
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('main.baseadm'))
    return render_template('empleados1/add.html')

# Ruta para editar un empleado existente
@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.apellido = request.form['apellido']
        empleado.email = request.form['email']
        empleado.telefono = request.form['telefono']
        empleado.password = request.form['password']
        empleado.cedula = request.form['cedula']
        
        db.session.commit()
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)

# Ruta para eliminar un empleado
@bp.route('/delete/<int:id>')
def delete(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))

# Ruta para ver las solicitudes de adopción pendientes
@bp.route('/solicitudes')
def solicitudes():
    solicitudes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    return render_template('solicitudes/index.html', solicitudes=solicitudes)

# Ruta para aprobar una solicitud de adopción
@bp.route('/aprobar/<int:id>', methods=['POST'])
def aprobar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Aprobada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

# Ruta para rechazar una solicitud de adopción
@bp.route('/rechazar/<int:id>', methods=['POST'])
def rechazar(id):
    solicitud = SolicitudAdopcion.query.get_or_404(id)
    solicitud.estado = 'Rechazada'
    db.session.commit()
    return redirect(url_for('empleado.solicitudes'))

# Ruta para ver los cuidados de un empleado (perros asignados)
@bp.route('/<int:id>/cuidados')
def cuidados(id):
    empleado = Empleado.query.get_or_404(id)
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    return render_template('empleados/cuidados.html', empleado=empleado, cuidados=cuidados)

# Ruta para el panel de control del empleado (dashboard)
@bp.route('/empleado/<int:id>/dashboard')
def dashboard(id):
    empleado = Empleado.query.get_or_404(id)
    solicitudes_pendientes = SolicitudAdopcion.query.filter_by(estado='Pendiente').all()
    cuidados = Cuidado.query.filter_by(empleado_id=empleado.id).all()
    perros = Perro.query.all()  # Para gestionar perros
    return render_template('empleados/dashboard.html', empleado=empleado, solicitudes_pendientes=solicitudes_pendientes, cuidados=cuidados, perros=perros)

# Ruta para archivos estáticos con url_for (añadido)
@bp.route('/static-file')
def static_file():
    return render_template('empleados/index.html', static_url=url_for('templates', filename='empleados/index.html'))



@bp.route('/perrosemple')
def perrosemple():
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
        return render_template('empleados/table.html', perros=perros)

    return render_template('empleados/perrosemple.html', perros=perros)

@bp.route('/empleado/perrosemple_nuevo', methods=['GET', 'POST'])
def perrosemple_nuevo():
    if request.method == 'POST':
        # Lógica para agregar un perro
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estado = request.form['estado']
        estadoSalud = request.form['estadoSalud']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        descripcion = request.form['descripcion']

        new_perro = Perro(
            nombre=nombre,
            raza=raza,
            edad=edad,
            estado=estado,
            estadoSalud=estadoSalud,
            color=color,
            fechaIngreso=fechaIngreso,
            descripcion=descripcion,
        )
        db.session.add(new_perro)
        db.session.commit()

        return redirect(url_for('empleado.perrosemple'))  # Redirigir a la lista de perros
    return render_template('empleados/perrosemple.html')






    # End Generation Here
