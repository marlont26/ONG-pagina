from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Veterinario
from app import db

bp = Blueprint('veterinario', __name__)

@bp.route('/veterinarios')
def index():
    veterinarios = Veterinario.query.all()
    return render_template('veterinarios/index.html', veterinarios=veterinarios)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        email = request.form['email']
        
        new_veterinario = Veterinario(
            nombre=nombre,
            apellido=apellido,
            especialidad=especialidad,
            telefono=telefono,
            email=email
        )
        db.session.add(new_veterinario)
        db.session.commit()
        
        return redirect(url_for('veterinario.index'))
    return render_template('veterinarios/create.html')

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
