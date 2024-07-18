from app import db

class SolicitudAdopcion(db.Model):
    __tablename__ = 'solicitud_adopcion'
    idSolicitud=db.Column(db.Integer, primary_key= True, autoincrement= True)
    fechaSolicitud = db.Column(db.Date)
    estado = db.Column(db.String(255))
    fechaAdopcion= db.Column(db.Date)
    comentarios = db.Column(db.String(255))
    
    empleado = db.Column(db.Integer, db.Foreignkey('empleado.idEmpleado'))
    adoptante= db.Column(db.Integer, db.Foreignkey('adoptante.idAdoptante'))  
    perro = db.Column(db.Integer, db.Foreignkey('perro.idPerro'))

