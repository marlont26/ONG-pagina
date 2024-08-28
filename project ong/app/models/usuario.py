from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from sqlalchemy import Enum
import enum

class Rol(enum.Enum):
    administrador = "administrador"
    empleado = "empleado"
    adoptante = "adoptante"
    veterinario = "veterinario"

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(Enum(Rol), nullable=False)
    fechaRegistro = db.Column(db.DateTime, default=db.func.current_timestamp())

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
