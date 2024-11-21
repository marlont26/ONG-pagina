from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.cuidado import Cuidado
from app.models.perro import Perro
from app.models.empleado import Empleado
from app.models.usuario import Usuario
from app import db

bp = Blueprint('cuidado', __name__)

@bp.route('/cuidados', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gestionar_cuidados():
    if request.method == 'GET':
        # Listar todos los cuidados
        cuidados = Cuidado.query.all()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify([{
                'id': c.id,
                'descripcion': c.descripcion,
                'fecha': c.fecha,
                'idPerro': c.idPerro,
                'idEmpleado': c.idEmpleado
            } for c in cuidados])
        return render_template('cuidados/index.html', cuidados=cuidados)

    elif request.method == 'POST':
        # Añadir un nuevo cuidado
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        idPerro = request.form['idPerro']
        idEmpleado = request.form['idEmpleado']
        
        nuevo_cuidado = Cuidado(
            descripcion=descripcion,
            fecha=fecha,
            idPerro=idPerro,
            idEmpleado=idEmpleado
        )
        db.session.add(nuevo_cuidado)
        db.session.commit()
        return redirect(url_for('cuidado.gestionar_cuidados'))

    elif request.method == 'PUT':
        # Editar un cuidado existente
        data = request.json
        cuidado = Cuidado.query.get_or_404(data['id'])
        cuidado.descripcion = data.get('descripcion', cuidado.descripcion)
        cuidado.fecha = data.get('fecha', cuidado.fecha)
        cuidado.idPerro = data.get('idPerro', cuidado.idPerro)
        cuidado.idEmpleado = data.get('idEmpleado', cuidado.idEmpleado)
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Cuidado actualizado correctamente'})

    elif request.method == 'DELETE':
        # Eliminar un cuidado
        cuidado_id = request.json.get('id')
        cuidado = Cuidado.query.get_or_404(cuidado_id)
        db.session.delete(cuidado)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Cuidado eliminado correctamente'})

    # Obtener datos para formularios (usado en vistas GET/POST si es necesario)
    perros = Perro.query.all()
    empleados = Empleado.query.join(Usuario).all()
    return render_template('cuidados/form.html', perros=perros, empleados=empleados)
