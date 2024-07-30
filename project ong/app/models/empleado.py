from app import db

class Empleado(db.Model):
    __tablename__ = 'empleado'
    idEmpleado = db.Column(db.Integer, primary_key= True, autoincrement=True)
    nombre= db.Column(db.String(255), nullable= True)
    apellido= db.Column(db.String(255), nullable=True)
    cargo = db.Column(db.string(155))
    telefono = db.Column(db.String(20))
    email= db.Column(db.String(255))
#perro_empleado relacion tabla intermedia = cuidado
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')
    #usuario = db.relationship('Usuario', back_populates='empleado', uselist=False)
