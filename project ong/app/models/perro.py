from app import db

class Perro(db.Model):
    __tablename__ = 'perro'
    idPerro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    estadoSalud = db.Column(db.String(255))
    estado = db.Column(db.String(255))
    color = db.Column(db.String(100))
    fechaIngreso = db.Column(db.Date)
    imagen = db.Column(db.String(255))
    descripcion = db.Column(db.Text)

    # Relaciones
    visitas_medicas = db.relationship('VisitaMedica', back_populates='perro')
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='perro')
    cuidados = db.relationship('Cuidado', back_populates='perro')
