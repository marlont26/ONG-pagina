from app import db

class Veterinario(db.Model):
    __tablename__ = 'veterinario'
    idVeterinario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(255), nullable=True)
    cedula = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(10), nullable=False, default='veterinario')

    # Relaciones con otras tablas

    visitas_medicas = db.relationship('VisitaMedica', back_populates='veterinario')
