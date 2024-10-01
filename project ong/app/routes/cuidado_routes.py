from flask import Blueprint, render_template, request, redirect, url_for
from app.models.cuidado import Cuidado
from app.models.perro import Perro
from app.models.empleado import Empleado
from app.models.usuario import Usuario



from app import db

bp = Blueprint('cuidado', __name__)

@bp.route('/cuidados')
def index():
    cuidados = Cuidado.query.all()
    return render_template('cuidados/index.html', cuidados=cuidados)

@bp.route('/add/cuidados', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        idPerro = request.form['idPerro']  # Cambiado de 'perro'
        idEmpleado = request.form['idEmpleado']  # Cambiado de 'empleado'
        
        new_cuidado = Cuidado(
            descripcion=descripcion,
            fecha=fecha,
            idPerro=idPerro,
            idEmpleado=idEmpleado
        )
        db.session.add(new_cuidado)
        db.session.commit()
        
        return redirect(url_for('cuidado.index'))
    perros = Perro.query.all()
    empleados = Empleado.query.join(Usuario).all()
    return render_template('cuidados/add.html', perros=perros, empleados=empleados)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cuidado = Cuidado.query.get_or_404(id)

    if request.method == 'POST':
        cuidado.descripcion = request.form['descripcion']
        cuidado.fecha = request.form['fecha']
        cuidado.idPerro = request.form['idPerro']  # Cambiado de 'perro'
        cuidado.idEmpleado = request.form['idEmpleado']  # Cambiado de 'empleado'
        
        db.session.commit()
        
        return redirect(url_for('cuidado.index'))

    perros = Perro.query.all()
    empleados = Empleado.query.all()
    return render_template('cuidados/edit.html', cuidado=cuidado, perros=perros, empleados=empleados)

@bp.route('/delete/<int:id>')
def delete(id):
    cuidado = Cuidado.query.get_or_404(id)
    
    db.session.delete(cuidado)
    db.session.commit()

    return redirect(url_for('cuidado.index'))
