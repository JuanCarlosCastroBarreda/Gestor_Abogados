from flask import Blueprint

bp = Blueprint("expedientes", __name__)

@bp.route("/")
def inicio():
    return "Bienvenido al sistema de expedientes 🧙‍♂️"
