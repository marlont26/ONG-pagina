from app import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'

    idLoan = db.Column(db.Integer, primary_key=True)
    loanDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    returnDate = db.Column(db.DateTime, nullable=True)
    fine = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), nullable=False, default='Active')

    # Relaciones
    bookId = db.Column(db.Integer, db.ForeignKey('books.idBook'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)

    book = db.relationship('Book', back_populates="loans", lazy=True)
    user = db.relationship('User', back_populates="loansUser", lazy=True)

    def __repr__(self):
        return f'<Loan {self.idLoan} of Book {self.bookId} to User {self.userId}>'