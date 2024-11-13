from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models.perro import Perro
from app.models.mensaje_contacto import MensajeContacto
from app import db
from datetime import datetime
from werkzeug.utils import secure_filename
import os

bp = Blueprint('perrojson', __name__, url_prefix='/perrosgod')

@bp.route('/perrostt', methods=['GET'])
def get_perros():
    perros = Perro.query.all()
    return jsonify([perro.to_json() for perro in perros]), 200, {'Content-Type': 'application/json'}
    

@bp.route('/addperro', methods=['POST'])
def addperro():
    print("entra al añadir perro")
    data = request.json
    new_perro = Perro(
        nombre=data['nombre'],
        raza=data['raza'],
        edad=data['edad'],
        fechaIngreso=data['fechaIngreso'],
        estadoSalud=data['estadoSalud'],  
        tamaño=data['tamaño'],
        genero=data['genero'],
        color=data['color'],  
        imagen=data['imagen'],
        descripcion=data['descripcion']
    )
    db.session.add(new_perro)
    db.session.commit()
    return jsonify({'message': 'Perro created successfully'}), 201

@bp.route('/editperro/<int:id>', methods=['PUT'])
def updatedog(id):
    perro = Perro.query.get(id)
    if perro:
        perro.nombre = request.json['nombre']
        perro.raza = request.json['raza']
        perro.edad = request.json['edad']
        perro.fechaIngreso = request.json['fechaIngreso']
        perro.estadoSalud = request.json['estadoSalud']
        perro.tamaño = request.json['tamaño']
        perro.genero = request.json['genero']
        perro.color = request.json['color']
        perro.imagen = request.json['imagen']
        perro.descripcion = request.json['descripcion']
        db.session.commit()
        return jsonify({'message': 'Perro updated successfully'})
    return jsonify({'message': 'Perro not found'}), 404

@bp.route('/deleteperro/<int:id>', methods=['DELETE'])
def deleteperro(id):
    perro = Perro.query.get(id)
    if perro:
        db.session.delete(perro)
        db.session.commit()
        return jsonify({'message': 'Perro deleted successfully'})
    return jsonify({'message': 'Perro not found'}), 404
