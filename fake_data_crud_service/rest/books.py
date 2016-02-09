from flask import Blueprint


books = Blueprint('books', __name__)


@books.route('/')
def say_hallo_service():
    return 'Books blueprint'


@books.route('/<name>/')
def say_hallo_to_guest_service(name):
    return 'Hallo ' + name
