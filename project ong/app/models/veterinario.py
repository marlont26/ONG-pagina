from app import db
from app.models.usuario import Usuario

class Veterinario(Usuario):
    __tablename__ = 'veterinario'
    idVete = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True, autoincrement=True)
    # Relaciones específicas de Veterinario
    visitas_medicas = db.relationship('VisitaMedica', back_populates='veterinario')
