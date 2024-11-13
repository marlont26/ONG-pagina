from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.models.cloans import ComputerLoan
from app.models.computers import Computer
from app.models.users import User
from datetime import datetime

bp = Blueprint('cloans', __name__, url_prefix='/cloans')


@bp.route('/', methods=['GET'])
def index():
    loans = ComputerLoan.query.all()
    return render_template('cloans/index.html', loans=loans)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        computerId = request.form['computerId']
        userId = request.form['userId']
        loanDate = request.form.get('loanDate', datetime.utcnow())
        returnDate = request.form.get('returnDate')
        status = request.form.get('status', 'Active')
        
        new_loan = ComputerLoan(
            computerId=computerId,
            userId=userId,
            loanDate=loanDate,
            returnDate=returnDate,
            status=status
        )
        db.session.add(new_loan)
        db.session.commit()
        return redirect(url_for('cloans.index'))
    
    computers = Computer.query.all()
    users = User.query.all()
    return render_template('cloans/add.html', computers=computers, users=users)

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def edit(id):
    loan = ComputerLoan.query.get_or_404(id)
    if request.method == 'POST':
        loan.computerId = request.form['computerId']
        loan.userId = request.form['userId']
        loan.loanDate = request.form['loanDate']
        loan.returnDate = request.form['returnDate']
        loan.status = request.form['status']
        db.session.commit()
        return redirect(url_for('cloans.index'))
    
    computers = Computer.query.all()
    users = User.query.all()
    return render_template('cloans/edit.html', loan=loan, computers=computers, users=users)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    loan = ComputerLoan.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return redirect(url_for('cloans.index'))

@bp.route('/return/<int:id>', methods=['POST'])
def return_computer(id):
    loan = ComputerLoan.query.get_or_404(id)
    loan.status = 'Returned'
    loan.returnDate = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('cloans.index'))
