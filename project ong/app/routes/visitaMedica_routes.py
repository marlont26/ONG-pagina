from flask import Blueprint, render_template, request, redirect, url_for
from app.models import VisitaMedica, Perro, Veterinario
from app import db

bp = Blueprint('visita_medica', __name__)

@bp.route('/visitasmedicas')
def index():
    visitas = VisitaMedica.query.all()
    return render_template('visitasmedicas/index.html', visitas=visitas)

@bp.route('/add/visitasmedicas', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha = request.form['fecha']
        descripcion = request.form['descripcion']
        idPerro = request.form['idPerro']  # Asegúrate que este sea el nombre correcto del formulario
        idVeterinario = request.form['idVeterinario']  # Asegúrate que este sea el nombre correcto del formulario
        
        new_visita = VisitaMedica(
            fecha=fecha,
            descripcion=descripcion,
            idPerro=idPerro,
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
        visita.idPerro = request.form['idPerro']  # Asegúrate que este sea el nombre correcto del formulario
        visita.idVeterinario = request.form['idVeterinario']  # Asegúrate que este sea el nombre correcto del formulario
        
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