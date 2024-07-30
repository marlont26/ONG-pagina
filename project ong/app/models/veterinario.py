from app import db

class Veterinario(db.Model):

    __tablename__='veterinario'
    idVeterinario = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nombre=db.Column(db.String(255), nullable= True)
    apellido=db.Column(db.String(255), nullable=True)
    telefono= db.Column(db.Integer)
    email= db.Column(db.String(255))
    especialidad=db.Column(db.String(255))


    visitas_medicas = db.relationship('VisitaMedica', back_populates='veterinario')





