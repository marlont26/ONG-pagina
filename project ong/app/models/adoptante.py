from app import db

class Adoptante(db.Model):
    __tablename__='adoptante'
    idAdoptante = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nombre = db.Column(db.String(255), nullable=True)
    apellido = db.Column(db.String(255), nullable=True)
    pais = db.Column(db.String(255))
    ciudad = db.Column(db.String(255))
    direccion= db.Column(db.String(255))
    telefono = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='adoptante')