from flask import Blueprint, render_template, request, redirect, url_for, flash
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
        motivo = request.form['motivo']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        idPerro = request.form['idPerro']
        
        # Validación de los datos antes de agregar
        if not all([fecha, motivo, diagnostico, tratamiento, idPerro]):
            flash('Todos los campos son requeridos.', 'danger')
            return redirect(url_for('visita_medica.add'))
        
        new_visita = VisitaMedica(
            fecha=fecha,
            motivo=motivo,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            idPerro=idPerro,
        )
        db.session.add(new_visita)
        db.session.commit()
        
        flash('Visita médica creada exitosamente.', 'success')
        return redirect(url_for('visita_medica.index'))
    
    perros = Perro.query.all()
    return render_template('visitasmedicas/add.html', perros=perros)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    visita = VisitaMedica.query.get_or_404(id)

    if request.method == 'POST':
        visita.fecha = request.form['fecha']
        visita.motivo = request.form['motivo']
        visita.diagnostico = request.form['diagnostico']
        visita.tratamiento = request.form['tratamiento']
        visita.idPerro = request.form['idPerro']
        
        db.session.commit()
        flash('Visita médica actualizada exitosamente.', 'success')
        return redirect(url_for('visita_medica.index'))

    perros = Perro.query.all()
    return render_template('visitasmedicas/edit.html', visita=visita, perros=perros)

@bp.route('/delete/<int:id>')
def delete(id):
    visita = VisitaMedica.query.get_or_404(id)
    
    db.session.delete(visita)
    db.session.commit()
    flash('Visita médica eliminada exitosamente.', 'success')

    return redirect(url_for('visita_medica.index'))
