from flask import Blueprint, render_template, request, redirect, url_for
from app.models.authors import Author
from app import db

bp = Blueprint('author', __name__, url_prefix='/Author')

@bp.route('/')
def index():
    authors = Author.query.all()   
    return render_template('authors/index.html', data=authors)

@bp.route('/list/<int:id>', methods=['GET', 'POST'])
def list(id):
    author = Author.query.get_or_404(id)
    books = author.books
    return render_template('authors/list.html', books=books)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nameAuthor = request.form['nameAuthor']
        nationalityAuthor = request.form['nationalityAuthor']
        new_author = Author(nameAuthor=nameAuthor, nationalityAuthor=nationalityAuthor)
        db.session.add(new_author)
        db.session.commit()
        
        return redirect(url_for('author.index'))

    return render_template('authors/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    author = Author.query.get_or_404(id)

    if request.method == 'POST':
        author.nameAuthor = request.form['nameAuthor']
        author.nationalityAuthor = request.form['nationalityAuthor']
        db.session.commit()
        return redirect(url_for('author.index'))

    return render_template('authors/edit.html', author=author)
    

@bp.route('/delete/<int:id>')
def delete(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()

    return redirect(url_for('author.index'))