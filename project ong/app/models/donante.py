from app import db

class Donante(db.Model):
    __tablename__='donante'
    idDonante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    pais = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)

    donaciones = db.relationship('Donacion', back_populates='donante')