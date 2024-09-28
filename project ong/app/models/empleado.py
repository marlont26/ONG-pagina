from app import db
from flask_login import UserMixin
from app.models.usuario import Usuario

class Empleado(Usuario, UserMixin):
    __tablename__ = 'empleado'
    idEmple = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    
    # Relaciones específicas de Empleado
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='empleado')
    cuidados = db.relationship('Cuidado', back_populates='empleado')

    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
        'inherit_condition': (idEmple == Usuario.id)
    }

    def get_id(self):
        return str(self.idEmple)