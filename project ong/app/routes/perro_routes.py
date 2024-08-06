from flask import Blueprint, render_template, request, redirect, url_for
from app.models.perro import Perro
from app import db

bp = Blueprint('perro', __name__)

@bp.route('/perros')
def index():
    perros = Perro.query.all()
    return render_template('perros/index.html', perros=perros)

@bp.route('/add/perros', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estado = request.form['estado']
        estadoSalud = request.form['estadoSalud']
        color = request.form['color']
        foto= request.form['foto']
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
            foto=foto
        )
        db.session.add(new_perro)
        db.session.commit()
        
        return redirect(url_for('perro.index'))
    return render_template('perros/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
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
        perro.foto = request.form['foto']
        perro.descripcion = request.form['descripcion']
        
        db.session.commit()
        
        return redirect(url_for('perro.index'))

    return render_template('perros/edit.html', perro=perro)

@bp.route('/delete/<int:id>')
def delete(id):
    perro = Perro.query.get_or_404(id)
    
    db.session.delete(perro)
    db.session.commit()

    return redirect(url_for('perro.index'))

@bp.route('/show/<int:id>')
def show(id):
    perro = Perro.query.get_or_404(id)
    return render_template('perros/show.html', perro=perro)


        