from app import db

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitud_adopcion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha = db.Column(db.Date)
    estado = db.Column(db.String(50), default='pendiente')  # Nuevo campo para el estado
    
    perro = db.relationship('Perro', back_populates='solicitudes_adopcion')
    usuario = db.relationship('Usuario', back_populates='solicitudes_adopcion')
