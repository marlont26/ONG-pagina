from app import db

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    nombre= db.Column(db.String(255), nullable= True)
    apellido= db.Column(db.String(255), nullable=True)
    cargo = db.Column(db.string(155))
    telefono = db.Column(db.String(20))
    email= db.Column(db.String(255))

    perros = db.relationship('Perro', secondary= 'cuidado')#perro_empleado relacion tabla intermedia = cuidado
    