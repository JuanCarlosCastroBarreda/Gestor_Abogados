from flask import Flask
from app.presentacion.controlador_expediente import bp as expediente_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(expediente_bp)
    return app
