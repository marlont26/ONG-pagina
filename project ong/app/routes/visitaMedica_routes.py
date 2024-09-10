from flask import Blueprint, render_template, request, redirect, url_for
from app.models import VisitaMedica, Perro, Veterinario
from app import db

bp = Blueprint('visita_medica', __name__)

@bp.route('/visitasmedicas')
def index():
    visitas = VisitaMedica.query.all()
    return render_template('visita_medica/index.html', visitas=visitas)

@bp.route('/add/visitasmedicas', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']
        perro_id = request.form['perro_id']
        idVeterinario = request.form['idVeterinario']
        
        new_visita = VisitaMedica(
            fecha=fecha,
            descripcion=descripcion,
            perro_id=perro_id,
            idVeterinario=idVeterinario
            )
        db.session.add(new_visita)
        db.session.commit()
        
        return redirect(url_for('visita_medica.index'))
    
    perros = Perro.query.all()
    veterinarios = Veterinario.query.all()
    return render_template('visitasmedicas/add.html', perros=perros, veterinarios=veterinarios)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    visita = VisitaMedica.query.get_or_404(id)

    if request.method == 'POST':
        visita.fecha = request.form['fecha']
        visita.descripcion = request.form['descripcion']
        visita.idPerro = request.form['idPerro']
        visita.idVeterinario = request.form['idVeterinario']
        
        db.session.commit()
        
        return redirect(url_for('visita_medica.index'))

    perros = Perro.query.all()
    veterinarios = Veterinario.query.all()
    return render_template('visitasmedicas/edit.html', visita=visita, perros=perros, veterinarios=veterinarios)

@bp.route('/delete/<int:id>')
def delete(id):
    visita = VisitaMedica.query.get_or_404(id)
    
    db.session.delete(visita)
    db.session.commit()

    return redirect(url_for('visita_medica.index'))

@bp.route('/<int:id>')
def show(id):
    visita = VisitaMedica.query.get_or_404(id)
    return render_template('visitasmedicas/show.html', visita=visita)
