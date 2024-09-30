from app import db
from app.models.usuario import Usuario

class Empleado(Usuario):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    
    # Relaciones específicas de Empleado
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')    

    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
    }

