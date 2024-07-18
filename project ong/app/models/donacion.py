from app import db

class Donacion(db.Model): 
    __tablename__ = 'donacion'
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    monto = db.Column(db.Integer)
    fechaDonacion = db.Column(db.Date)

    #llave foranea de donante 
    donante = db.Column(db.Integer, db.primarykey('donante.idDonante'))
