from app import db

class Cuidado(db.Model):
    __tablename__ = 'cuidado'
    idCuidado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    idEmple = db.Column(db.Integer, db.ForeignKey('empleado.idEmple'))
    descripcion = db.Column(db.String(255))
    fecha = db.Column(db.Date)

    # Relaciones
    perro = db.relationship('Perro', back_populates='cuidados')
    empleado = db.relationship('Empleado', back_populates='cuidados')sd
