from app import db

class Perro(db.Model):
    __tablename__ = 'perro'
    idPerro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    raza = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    estadoSalud = db.Column(db.String(255))
    color = db.Column(db.String(255))
    fechaIngreso = db.Column(db.Date)
    imagen = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    tamaño = db.Column(db.String(255))
    genero = db.Column(db.String(100))
    estado = db.Column(db.String(255))  

    # Relaciones
    visitas_medicas = db.relationship('VisitaMedica', back_populates='perro')
    solicitudes_adopcion = db.relationship('SolicitudAdopcion', back_populates='perro')
    cuidados = db.relationship('Cuidado', back_populates='perro')

    def to_json(self):
        return {
            "idPerro": self.idPerro,
            "nombre": self.nombre,
            "raza" : self.raza,
            "edad" : self.edad,
            "estadoSalud" : self.estadoSalud,
            "color" : self.color,
            "fechaIngreso" : self.fechaIngreso,
            "imagen" : self.imagen,
            "descripcion" : self.descripcion,
            "tamaño" : self.tamaño,
            "genero" : self.genero,
        }
