from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from flask_cors import CORS, cross_origin
import os

# from dotenv import load_dotenv

########################################################
#                                  This section is set to configure our application                         #
########################################################

# The following line helps to get all the environment variables from .env
# load_dotenv()

# Initial configurations
app = Flask(__name__)

username = os.getenv('user')
password = quote_plus(os.getenv('password'))
host = os.getenv('host')
port = os.getenv('port')
db_name = os.getenv('db_name')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
    return response


# Classes that represent our tables
class Categorie(db.Model):
    __tablename__ = 'categories'
    id_categorie = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(), nullable=False)
    livres = db.relationship('Livre', backref='categories', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id_categorie,
            'libelle': self.libelle
        }


class Livre(db.Model):
    __tablename__ = 'livres'
    id_livre = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(30), unique=True, nullable=False)
    titre = db.Column(db.String(80), unique=True, nullable=False)
    date_publication = db.Column(db.Date(), nullable=False)
    auteur = db.Column(db.String(), nullable=False)
    editeur = db.Column(db.String(), nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey(Categorie.id_categorie))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id_livre,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'id_categorie': self.id_categorie
        }


db.create_all()


def format(items):
    return [item.format() for item in items]


########################################################
#         This section is set to add the different endpoints of our application               #
########################################################

# Endpoint of base
@app.route('/')
def index():
    return jsonify({
        "message": "The more that you read, the more things you will know.",
        "ps": "If you don't like to read, you haven't found the right book"
    })


# Endpoint 'List of all the books'
@app.route('/livres')
def all_books():
    books = Livre.query.all()
    books = format(books)
    return jsonify({
        'success': True,
        'total_books': len(books),
        'book': books
    })


# Endpoint 'Get a book by its id'
@app.route('/livres/<int:id>')
def book(id):
    book = Livre.query.get(id)
    if book is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'selected_id': id,
            'book': book.format()
        })


# Endpoint 'List of all books from a category'
@app.route('/categories/<int:id>/livres')
def books_category(id):
    books = Livre.query.filter(Livre.id_categorie == id).all()
    books = format(books)
    if books is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'total_books': len(books),
            'book(s)': books
        })


# Endpoint 'Get a category by its id'
@app.route('/categories/<int:id>')
def category(id):
    category = Categorie.query.get(id)
    if category is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'selected_id': id,
            'category': category.format()
        })


# Endpoint 'List of all the categories'
@app.route('/categories')
def all_categories():
    categories = Categorie.query.all()
    categories = format(categories)
    return jsonify({
        'success': True,
        'total_categories': len(categories),
        'category': categories
    })


# Endpoint 'Delete a book'
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Livre.query.get(id)
    if book is None:
        abort(404)
    else:
        book.delete()
        return jsonify({
            'success': True,
            'deleted_id': id,
            'book': book.format(),
            'total_books': Livre.query.count()
        })


# Endpoint 'Delete a category'
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Categorie.query.get(id)
    if category is None:
        abort(404)
    else:
        books = Livre.query.filter(Livre.id_categorie == id).all()
        if len(books) != 0:
            abort(405)
        else:
            category.delete()
            return jsonify({
                'success': True,
                'deleted_id': id,
                'category': category.format(),
                'total_categories': Categorie.query.count()
            })


# Endpoint 'Edit a book'
@app.route('/livres/<int:id>', methods=['PATCH'])
def edit_book(id):
    book = Livre.query.get(id)
    if book is None:
        abort(404)
    else:
        body = request.get_json()
        editable_columns = [
            'isbn',
            'titre',
            'date_publication',
            'auteur',
            'editeur',
            'id_categorie'
        ]
        for info in body:
            match info:
                case 'isbn':
                    book.isbn = body['isbn']
                case 'titre':
                    book.titre = body['titre']
                case 'auteur':
                    book.auteur = body['auteur']
                case 'editeur':
                    book.editeur = body['editeur']
                case 'id_categorie':
                    book.id_categorie = body['id_categorie']
                case 'date_publication':
                    book.date_publication = body['date_publication']
                case _:
                    continue
        book.update()
        return jsonify({
            'success': True,
            'info_edited': [info for info in body if info in editable_columns],
            'book': book.format()
        })


# Endpoint 'Edit the libel of a category'
@app.route('/categories/<int:id>', methods=['PATCH'])
def edit_category(id):
    category = Categorie.query.get(id)
    if category is None:
        abort(404)
    else:
        body = request.get_json()
        if 'libelle' in body:
            category.libelle = body['libelle']
        category.update()
        return jsonify(({
            'success': True,
            'category': category.format()
        }))


########################################################
#         This section is set to handle different errors while sending requests              #
########################################################

@app.errorhandler(404)
def client(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Not found'
    }), 404


@app.errorhandler(405)
def method(error):
    return jsonify(({
        'success': False,
        'error': 405,
        'message': 'Not allowed'
    })), 405


@app.errorhandler(500)
def server(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal Server Error'
    }), 500
