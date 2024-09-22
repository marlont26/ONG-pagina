from app import db

class MensajeContacto(db.Model):
    __tablename__ = 'mensaje_contacto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    asunto = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.String(100), nullable=False)


   
