from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Donante, Donacion
from app import db

bp_donante = Blueprint('donante', __name__)

@bp_donante.route('/')
def index():
    donantes = Donante.query.all()
    return render_template('donantes/index.html', donantes=donantes)

@bp_donante.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        
        new_donante = Donante(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        db.session.add(new_donante)
        db.session.commit()
        
        return redirect(url_for('donante.index'))
    return render_template('donantes/create.html')

@bp_donante.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    donante = Donante.query.get_or_404(id)

    if request.method == 'POST':
        donante.nombre = request.form['nombre']
        donante.apellido = request.form['apellido']
        donante.email = request.form['email']
        donante.telefono = request.form['telefono']
        
        db.session.commit()
        
        return redirect(url_for('donante.index'))

    return render_template('donantes/edit.html', donante=donante)

@bp_donante.route('/delete/<int:id>')
def delete(id):
    donante = Donante.query.get_or_404(id)
    
    db.session.delete(donante)
    db.session.commit()

    return redirect(url_for('donante.index'))

@bp_donante.route('/<int:id>/donaciones')
def donaciones(id):
    donante = Donante.query.get_or_404(id)
    return render_template('donantes/donaciones.html', donante=donante)
