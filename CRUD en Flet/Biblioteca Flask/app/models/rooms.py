from sqlalchemy import Column, Integer, String
from app import db

class Room(db.Model):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)  # Especificar longitud
    description = Column(String(255), index=True)  # Especificar longitud

    def __repr__(self):
        return f'<Room {self.id} - {self.name}>'
