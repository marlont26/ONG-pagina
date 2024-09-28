from app import db

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitud_adopcion'
    idSolicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    idAdoptante = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    fechaSolicitud = db.Column(db.Date)
    estado = db.Column(db.String(255))
    idEmpleado = db.Column(db.Integer, db.ForeignKey('empleado.idEmple'))  # Asegúrate de que 'idEmpleado' exista en 'empleado'
    comentarios = db.Column(db.String(255))
    
    perro = db.relationship('Perro', back_populates='solicitudes_adopcion')
    empleado = db.relationship('Empleado', back_populates='solicitudes_adopcion', foreign_keys=[idEmpleado])
    adoptante = db.relationship('Usuario', back_populates='solicitudes_adopcion')