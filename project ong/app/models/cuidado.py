from app import db

class Cuidado(db.Model):
    __tablename__ = 'cuidado' 
    idCuidado = db.Column(db.Integer, primary_key=True)
    idPerro = db.Column(db.Integer, db.foreignkey('perro.idPerro'))
    idEmpleado =db.Column(db.Integer, db.foreignkey('empleado.idEmpleado'))
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
    #relaciones
    empleado = db.relationship('Empleado', back_populates='cuidados')
    perro = db.relationship('Perro', back_populates='cuidados')