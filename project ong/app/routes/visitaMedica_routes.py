from flask import Blueprint, render_template, request, redirect, url_for
from app.models import VisitaMedica, Perro, Veterinario
from app import db

bp_visita_medica = Blueprint('visita_medica', __name__)

@bp_visita_medica.route('/')
def index():
    visitas = VisitaMedica.query.all()
    return render_template('visita_medica/index.html', visitas=visitas)

@bp_visita_medica.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']
        perro_id = request.form['perro_id']
        veterinario_id = request.form['veterinario_id']
        
        new_visita = VisitaMedica(
            fecha=fecha,
            descripcion=descripcion,
            perro_id=perro_id,
            veterinario_id=veterinario_id
        )
        db.session.add(new_visita)
        db.session.commit()
        
        return redirect(url_for('visita_medica.index'))
    
    perros = Perro.query.all()
    veterinarios = Veterinario.query.all()
    return render_template('visita_medica/add.html', perros=perros, veterinarios=veterinarios)

@bp_visita_medica.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    visita = VisitaMedica.query.get_or_404(id)

    if request.method == 'POST':
        visita.fecha = request.form['fecha']
        visita.descripcion = request.form['descripcion']
        visita.perro_id = request.form['perro_id']
        visita.veterinario_id = request.form['veterinario_id']
        
        db.session.commit()
        
        return redirect(url_for('visita_medica.index'))

    perros = Perro.query.all()
    veterinarios = Veterinario.query.all()
    return render_template('visita_medica/edit.html', visita=visita, perros=perros, veterinarios=veterinarios)

@bp_visita_medica.route('/delete/<int:id>')
def delete(id):
    visita = VisitaMedica.query.get_or_404(id)
    
    db.session.delete(visita)
    db.session.commit()

    return redirect(url_for('visita_medica.index'))

@bp_visita_medica.route('/<int:id>')
def show(id):
    visita = VisitaMedica.query.get_or_404(id)
    return render_template('visita_medica/show.html', visita=visita)
