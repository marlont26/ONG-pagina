from app import db

class Computer(db.Model):
    __tablename__ = 'computers'

    idComputer = db.Column(db.Integer, primary_key=True)
    brandComputer = db.Column(db.String(50), nullable=False)
    modelComputer = db.Column(db.String(50), nullable=False)
    statusComputer = db.Column(db.String(20), nullable=False, default='Active')

    # Relación inversa
    computerLoans = db.relationship('ComputerLoan', back_populates='computer', lazy=True)

    def __repr__(self):
        return f'<Computer {self.idComputer} - {self.brandComputer} {self.modelComputer}>'
