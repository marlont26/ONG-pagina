from app import db

class Perro(db.Model):
    __tablename__='perro'
    idPerro= db.Column(db.Integer,primary_key=True, autoincrement= True)
    nombre= db.Column(db.String(255), nullable=False)
    raza=db.Colum(db.String(255))
    edad= db.Column(db.Integer)
    estadoSalud= db.Column(db.String(255))
    estado=db.Column(db.String(255))
    color=db.Column(db.String(255))
    fechaIngreso=db.Column(db.String(255))
    foto=db.Column(db.String(255))
    descripcion= db.Column(db.String(255))
    
    #relacion con la tabla empleado a traves de la tabla Cuiddado que es la intermedia
    empleado = db.relationship('Empleado', secondary='cuidado')#empleado_perro relacion para la tabla intermedia = cuidado