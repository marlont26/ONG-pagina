from app import db

class VisitaMedica(db.Model):
    __tablename__ = 'visita_medica'
    idVistiamedica= db.Column(db.Integer, primary_key=True, autoincrement= True)
    idPerro = db.Column(db.Integer, db.ForeignKey('perro.idPerro'))
    fecha = db.Column(db.Date)
    descripcion= db.Column(db.String(255))
    idVeterinario = db.Column(db.Integer, db.ForeignKey('veterinario.idVete'))
    
    perro = db.relationship('Perro', back_populates='visitas_medicas')
    veterinario = db.relationship('Veterinario', back_populates='visitas_medicas')