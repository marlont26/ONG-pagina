from app import db

class Empleado(db.Model):
    __tablename__ = 'empleado'
    idEmpleado = db.Column(db.Integer, primary_key= True, autoincrement=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    nombre= db.Column(db.String(255), nullable= True)
    apellido= db.Column(db.String(255), nullable=True)
    telefono = db.Column(db.String(20))
    email= db.Column(db.String(255))
#perro_empleado relacion tabla intermedia = cuidado
    usuario = db.relationship('Usuario', back_populates='empleado')
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')
    #usuario = db.relationship('Usuario', back_populates='empleado', uselist=False)
