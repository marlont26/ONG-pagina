from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))  # Asegúrate de que este campo sea lo suficientemente largo para almacenar la contraseña encriptada
    telefono = db.Column(db.String(20))
    cedula = db.Column(db.String(20))
    rol = db.Column(db.String(20))  # Asegúrate de que este campo exista
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='adoptante', lazy=True)
    empleado = db.relationship('Empleado', backref='usuario', uselist=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.id)
