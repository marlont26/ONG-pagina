from app import db
from app.models.usuario import Usuario

class Empleado(Usuario):
    __tablename__ = 'empleado'
    idEmple = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    
    # Relaciones específicas de Empleado
    usuario = db.relationship('Usuario', backref='empleado', uselist=False)
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')    
    
