from app import db
class Author(db.Model):
    __tablename__ = 'authors'
    idAuthor = db.Column(db.Integer, primary_key=True)
    nameAuthor = db.Column(db.String(255), nullable=False)
    nationalityAuthor = db.Column(db.String(255), nullable=False)
    
    books = db.relationship("Book", back_populates="author", lazy='dynamic')
    
    def __repr__(self):
        return f'<Author {self.nameAuthor}>'
   
