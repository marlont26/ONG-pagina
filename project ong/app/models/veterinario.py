from app import db

class Veterinario(db.Model):
    __tablename__ = 'veterinario'
    idVeterinario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    especialidad = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Relaciones con otras tablas

    visitas_medicas = db.relationship('VisitaMedica', back_populates='veterinario')
