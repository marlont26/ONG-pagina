from app import db

from app.models.usuario import Usuario
from app import db

class Veterinario(Usuario):
    __tablename__ = 'veterinario'
    idVete = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'veterinario',
    }

    # Relaciones específicas de Veterinario
    visitas_medicas = db.relationship('VisitaMedica', back_populates='veterinario')
