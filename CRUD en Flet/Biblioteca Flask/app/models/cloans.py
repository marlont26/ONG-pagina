from app import db
from datetime import datetime

class ComputerLoan(db.Model):
    __tablename__ = 'computer_loans'

    idLoan = db.Column(db.Integer, primary_key=True)
    loanDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    returnDate = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Active')

    # Relaciones
    computerId = db.Column(db.Integer, db.ForeignKey('computers.idComputer'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.idUser'), nullable=False)

    computer = db.relationship('Computer', back_populates='computerLoans', lazy=True)
    user = db.relationship('User', back_populates='computerLoansUser', lazy=True)

    def __repr__(self):
        return f'<ComputerLoan {self.idLoan} of Computer {self.computerId} to User {self.userId}>'
