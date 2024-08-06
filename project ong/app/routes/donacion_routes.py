from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Donacion, Donante
from app import db

bp = Blueprint('donacion', __name__)

@bp.route('/donaciones')
def index():
    donaciones = Donacion.query.all()
    return render_template('donaciones/index.html', donaciones=donaciones)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        monto = request.form['monto']
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']
        donante_id = request.form['donante_id']
        
        new_donacion = Donacion(
            monto=monto,
            fecha=fecha,
            descripcion=descripcion,
            donante_id=donante_id
        )
        db.session.add(new_donacion)
        db.session.commit()
        
        return redirect(url_for('donacion.index'))
    donantes = Donante.query.all()
    return render_template('donaciones/add.html', donantes=donantes)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    donacion = Donacion.query.get_or_404(id)

    if request.method == 'POST':
        donacion.monto = request.form['monto']
        donacion.fecha = request.form['fecha']
        donacion.descripcion = request.form['descripcion']
        donacion.donante_id = request.form['donante_id']
        
        db.session.commit()
        
        return redirect(url_for('donacion.index'))

    donantes = Donante.query.all()
    return render_template('donaciones/edit.html', donacion=donacion, donantes=donantes)

@bp.route('/delete/<int:id>')
def delete(id):
    donacion = Donacion.query.get_or_404(id)
    
    db.session.delete(donacion)
    db.session.commit()

    return redirect(url_for('donacion.index'))

@bp.route('/<int:id>/show')
def show(id):
    donacion = Donacion.query.get_or_404(id)
    return render_template('donaciones/show.html', donacion=donacion)
