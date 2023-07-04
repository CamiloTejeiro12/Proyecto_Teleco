from flask import Blueprint, jsonify

main = Blueprint('users_blueprint', __name__)


@main.route('/')
def get_movies():
    return jsonify({'message': 'Creación del servidor'}), 500
    