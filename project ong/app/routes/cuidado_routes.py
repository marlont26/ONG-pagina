from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Cuidado, Empleado, Perro
from app import db

bp_cuidado = Blueprint('cuidado', __name__)

@bp_cuidado.route('/')
def index():
    cuidados = Cuidado.query.all()
    return render_template('cuidados/index.html', cuidados=cuidados)

@bp_cuidado.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        perro_id = request.form['perro']
        empleado_id = request.form['empleado']
        
        new_cuidado = Cuidado(
            descripcion=descripcion,
            fecha=fecha,
            perro_id=perro_id,
            empleado_id=empleado_id
        )
        db.session.add(new_cuidado)
        db.session.commit()
        
        return redirect(url_for('cuidado.index'))
    perros = Perro.query.all()
    empleados = Empleado.query.all()
    return render_template('cuidados/create.html', perros=perros, empleados=empleados)

@bp_cuidado.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cuidado = Cuidado.query.get_or_404(id)

    if request.method == 'POST':
        cuidado.descripcion = request.form['descripcion']
        cuidado.fecha = request.form['fecha']
        cuidado.perro_id = request.form['perro']
        cuidado.empleado_id = request.form['empleado']
        
        db.session.commit()
        
        return redirect(url_for('cuidado.index'))

    perros = Perro.query.all()
    empleados = Empleado.query.all()
    return render_template('cuidados/edit.html', cuidado=cuidado, perros=perros, empleados=empleados)

@bp_cuidado.route('/delete/<int:id>')
def delete(id):
    cuidado = Cuidado.query.get_or_404(id)
    
    db.session.delete(cuidado)
    db.session.commit()

    return redirect(url_for('cuidado.index'))
