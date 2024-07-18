from app import db

class Cuidado(db.Model):
    __tablename__ = 'cuidado' 
    idCuidado = db.Column(db.Integer, primary_key=True)
    perros = db.Column(db.Integer, db.foreignkey('perro.idPerro'), primarykey=True)
    empleados =db.Column(db.Integer, db.foreignkey('empleado.idEmpleado'), primarykey= True)
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
