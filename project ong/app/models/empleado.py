from app import db

from app.models.usuario import Usuario
from app import db

class Empleado(Usuario):
    __tablename__ = 'empleado'
    idEmple = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
    }

    # Relaciones específicas de Empleado
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')
