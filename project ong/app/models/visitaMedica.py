from app import db

class visitaMedica(db.Model):
    __tablename__:'visita_medica'
    idVistiamedica= db.Column(db.Integer, primary_key=True, autoincrement= True)
    descripcionVisita= db.Column(db.String(255))


    perro=db.Column(db.Integer, db.foreignKey('perro.idPerro'))
    veterinario=db.Column(db.Integer, db.foreignKey('veterinario.idVeterinario'))
