from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.books import Book
from app.models.authors import Author
from app import db

bp = Blueprint('book', __name__, url_prefix='/Book')

@bp.route('/')
def index():
    data = Book.query.all()
    return render_template('books/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titleBook = request.form['titleBook']
        authorId = request.form['authorId']
        
        new_book = Book(titleBook=titleBook, authorId=authorId)
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('book.index'))
    
    data = Author.query.all()
    return render_template('books/add.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.titleBook = request.form['titleBook']
        book.authorId = request.form['authorId']
        db.session.commit()        
        return redirect(url_for('book.index'))

    authors = Author.query.all()
    return render_template('books/edit.html', book=book, authors=authors)

@bp.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get_or_404(id)    
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('book.index'))
