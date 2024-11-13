from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.models.computers import Computer

bp = Blueprint('computers', __name__, url_prefix='/computers')

@bp.route('/', methods=['GET'])
def index():
    computers = Computer.query.all()
    return render_template('computers/index.html', computers=computers)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        brandComputer = request.form['brandComputer']
        modelComputer = request.form['modelComputer']
        statusComputer = request.form['statusComputer']
        
        new_computer = Computer(
            brandComputer=brandComputer,
            modelComputer=modelComputer,
            statusComputer=statusComputer
        )
        db.session.add(new_computer)
        db.session.commit()
        return redirect(url_for('computers.index'))
    return render_template('computers/add.html')

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    computer = Computer.query.get_or_404(id)
    db.session.delete(computer)
    db.session.commit()
    return redirect(url_for('computers.index'))

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    computer = Computer.query.get_or_404(id)
    if request.method == 'POST':
        computer.brandComputer = request.form['brandComputer']
        computer.modelComputer = request.form['modelComputer']
        computer.statusComputer = request.form['statusComputer']
        db.session.commit()
        return redirect(url_for('computers.index'))
    return render_template('computers/edit.html', computer=computer)
