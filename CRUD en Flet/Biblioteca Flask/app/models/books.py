from app import db
class Book(db.Model):
    __tablename__ = 'books'
    idBook = db.Column(db.Integer, primary_key=True)
    titleBook = db.Column(db.String(255), nullable=False)
    authorId = db.Column(db.Integer, db.ForeignKey('authors.idAuthor'))  # Cambia el nombre de la columna para mayor claridad
    
    author = db.relationship("Author", back_populates="books", lazy=True)  # Cambia lazy a True
    loans = db.relationship("Loan", back_populates="book", lazy='dynamic')
    
    def __repr__(self):
        return f'<Book {self.titleBook}>'
