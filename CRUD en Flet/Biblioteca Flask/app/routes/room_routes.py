from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.rooms import Room
from app import db

bp = Blueprint('room', __name__, url_prefix='/room')

@bp.route('/')
def index():
    data = Room.query.all()
    return render_template('rooms/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_room = Room(name=name, description=description)
        db.session.add(new_room)
        db.session.commit()
        
        return redirect(url_for('room.index'))
    return render_template('rooms/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    room = Room.query.get_or_404(id)
    if request.method == 'POST':
        room.name = request.form['name']
        room.description = request.form['description']
        db.session.commit()
        return redirect(url_for('room.index'))

    return render_template('rooms/edit.html', room=room)

@bp.route('/delete/<int:id>')
def delete(id):
    room = Room.query.get_or_404(id)
    db.session.delete(room)
    db.session.commit()
    return redirect(url_for('room.index'))
