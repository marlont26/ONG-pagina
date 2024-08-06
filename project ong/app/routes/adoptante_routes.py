from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Adoptante, Perro, SolicitudAdopcion
from app import db

bp= Blueprint('adoptante', __name__)

@bp.route('/adoptantes')
def index():
    adoptantes = Adoptante.query.all()
    return render_template('adoptantes/index.html', adoptantes=adoptantes)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        pais = request.form['pais']
        ciudad = request.form['ciudad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        
        new_adoptante = Adoptante(
            nombre=nombre,
            apellido=apellido,
            pais=pais,
            ciudad=ciudad,
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        db.session.add(new_adoptante)
        db.session.commit()
        
        return redirect(url_for('adoptante.index'))
    return render_template('adoptantes/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    adoptante = Adoptante.query.get_or_404(id)

    if request.method == 'POST':
        adoptante.nombre = request.form['nombre']
        adoptante.apellido = request.form['apellido']
        adoptante.pais = request.form['pais']
        adoptante.ciudad = request.form['ciudad']
        adoptante.direccion = request.form['direccion']
        adoptante.telefono = request.form['telefono']
        adoptante.email = request.form['email']
        
        db.session.commit()
        
        return redirect(url_for('adoptante.index'))

    return render_template('adoptantes/edit.html', adoptante=adoptante)

@bp.route('/delete/<int:id>')
def delete(id):
    adoptante = Adoptante.query.get_or_404(id)
    
    db.session.delete(adoptante)
    db.session.commit()

    return redirect(url_for('adoptante.index'))

@bp.route('/show/<int:id>', methods=['GET', 'POST'])
def show(id):
    adoptante = Adoptante.query.get_or_404(id)
    
    if request.method == 'POST':
        if 'solicitar' in request.form:
            idPerro = request.form['idPerro']
            nueva_solicitud = SolicitudAdopcion(
                idAdoptante=adoptante.idAdoptante,
                idPerro=idPerro,
                estado='Pendiente'
            )
            db.session.add(nueva_solicitud)
            db.session.commit()
            return redirect(url_for('adoptante.show', id=adoptante.idAdoptante))
        
        if 'actualizar' in request.form:
            adoptante.nombre = request.form['nombre']
            adoptante.apellido = request.form['apellido']
            adoptante.pais = request.form['pais']
            adoptante.ciudad = request.form['ciudad']
            adoptante.direccion = request.form['direccion']
            adoptante.telefono = request.form['telefono']
            adoptante.email = request.form['email']
            db.session.commit()
            return redirect(url_for('adoptante.show', id=adoptante.idAdoptante))

    perros = Perro.query.all()
    return render_template('adoptantes/show.html', adoptante=adoptante, perros=perros)
