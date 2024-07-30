from app import db

class visitaMedica(db.Model):
    __tablename__:'visita_medica'
    idVistiamedica= db.Column(db.Integer, primary_key=True, autoincrement= True)
    idPerro = db.Column(db.Integer, db.ForeingKey('perro.idPerro'))
    fecha = db.Column(db,Date)
    descripcionVisita= db.Column(db.String(255))
    idVeterinario = db.Column(db.Integer, db.ForeignKey('veterinario.idVeterinario'))
    
    perro = db.relationship('Perro', back_populates='visitas_medicas')
    veterinario = db.relationship('Veterinario', back_populates='visitas_medicas')