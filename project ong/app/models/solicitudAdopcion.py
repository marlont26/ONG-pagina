from app import db

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitud_adopcion'
    idSolicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAdoptante = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    estado = db.Column(db.String(50))
    
    # Relaciones
    adoptante = db.relationship('Usuario', back_populates='solicitudes_adopcion')
    perro = db.relationship('Perro', back_populates='solicitudes_adopcion')
    empleado = db.relationship('Empleado', back_populates='solicitudes_adopcion')
