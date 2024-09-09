from flask_login import UserMixin
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    cedula = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(255))
    ciudad = db.Column(db.String(255))
    



