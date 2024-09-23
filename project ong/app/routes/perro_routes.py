from flask import Blueprint, render_template, request, redirect, url_for
from app.models.perro import Perro
from app import db

bp = Blueprint('perro', __name__)

@bp.route('/perros')
def index():
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
        return render_template('perros/table.html', perros=perros)

    return render_template('perros/index.html', perros=perros)

@bp.route('/add/perro', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
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
            estadoSalud=estadoSalud,
            fechaIngreso=fechaIngreso,
            descripcion=descripcion,
            estado=estado,
            color=color,
        )
        db.session.add(new_perro)
        db.session.commit()
        
        return redirect(url_for('perro.index'))
    return render_template('perros/add.html')

@bp.route('/editperro/<int:id>', methods=['GET', 'POST'])
def edit(id):
    perro = Perro.query.get_or_404(id)

    if request.method == 'POST':
        perro.nombre = request.form['nombre']
        perro.raza = request.form['raza']
        perro.edad = request.form['edad']
        perro.estadoSalud = request.form['estadoSalud']
        perro.estado = request.form['estado']
        perro.color = request.form['color']
        perro.fechaIngreso = request.form['fechaIngreso']
        perro.descripcion = request.form['descripcion']
        
        db.session.commit()
        return redirect(url_for('perro.index'))

    return render_template('perros/edit.html', perro=perro)

@bp.route('/deleteperro/<int:id>')
def delete(id):
    perro = Perro.query.get_or_404(id)
    
    db.session.delete(perro)
    db.session.commit()

    return redirect(url_for('perro.index'))

@bp.route('/showperro/<int:id>')
def show(id):
    perro = Perro.query.get_or_404(id)
    return render_template('perros/show.html', perro=perro)


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
        return render_template('empleados/table.html ', perros=perros)

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

        return redirect(url_for('empleado.index'))  # Redirigir al dashboard del empleado
    return render_template('empleados/perrosemple.html')





#@bp.route('/perrosemple')
#def perrosemple():
    #perros = Perro.query.paginate(page=1, per_page=10)
    #return render_template('perros/perrosemple.html', perros=perros)
