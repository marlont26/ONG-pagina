from app import db

class Donacion(db.Model): 
    __tablename__ = 'donacion'
    idDonacion = db.Column(db.Integer, primary_key=True, autoincrement= True)
    idDonante = db.Column(db.Integer, db.ForeignKey('donante.idDonante'))
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date)

    #llave foranea de donante 
    donante = db.relationship('Donante', back_populates='donaciones')