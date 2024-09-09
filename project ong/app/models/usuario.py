from flask_login import UserMixin
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fechaRegistro = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relación con Empleado
    empleados = db.relationship('Empleado', back_populates='usuario')

