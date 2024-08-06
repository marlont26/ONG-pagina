from app import db

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitud_adopcion'
    idSolicitud=db.Column(db.Integer, primary_key= True, autoincrement= True)
    idAdoptante = db.Column(db.Integer, db.ForeignKey('adoptante.idAdoptante'))
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    fechaSolicitud = db.Column(db.Date)
    estado = db.Column(db.String(255))
    idEmpleado = db.Column(db.Integer, db.ForeignKey('empleado.idEmpleado'))
    comentarios = db.Column(db.String(255))
    #relaciones con otras tabas
    
    adoptante = db.relationship('Adoptante', back_populates='solicitudes_adopcion')
    perro = db.relationship('Perro', back_populates='solicitudes_adopcion')
    empleado = db.relationship('Empleado', back_populates='solicitudes_adopcion')
