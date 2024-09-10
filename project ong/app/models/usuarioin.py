from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash


class Usuarioin(db.Model, UserMixin):
    __tablename__ = 'usuarioin'

    iduserin = Column(Integer, primary_key=True, autoincrement=True)
    nombrein = Column(String(50), nullable=False)
    emailin = Column(String(100), unique=True, nullable=False)
    passwordin = Column(String(128), nullable=False)
    veterinarioin = Column(Boolean, default=False)
    empleadoin = Column(Boolean, default=False)

    def set_password(self, password):
        self.passwordin = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordin, password)
    
    def get_id(self):
        return str(self.iduserin)