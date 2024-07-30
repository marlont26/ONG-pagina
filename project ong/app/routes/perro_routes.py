from flask import Blueprint, render_template, request, redirect, url_for
from app.models.perro import Perro
from app import db

bp = Blueprint('perro', __name__)

@bp.route('/perro')
def index():
    data = Perro.query.all()
    return render_template('perros/index.html', perros=data)

@bp.route('/add', methods=['GET','POST'])
def add():
    if request.method =='POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        estadoSalud = request.form['estadoSalud']
        estado = request.form['estado']
        color = request.form['color']
        fechaIngreso = request.form['fechaIngreso']
        foto = request.form['foto']
        descripcion = request.form['descripcion']

        new_perro = Perro(nombre=nombre, raza=raza, edad=edad, estadoSalud=estadoSalud, estado=estado, color=color, fechaIngreso=fechaIngreso, foto=foto, descripcion=descripcion)
        db.session.add(new_perro)
        db.session.commit()

        return redirect(url_for('perro.index'))
    data = 


        