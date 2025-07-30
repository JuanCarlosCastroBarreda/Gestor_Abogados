from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abogados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Importar modelos aquí para que SQLAlchemy los registre
    with app.app_context():
        from app.dominio.expediente import Expediente
        db.create_all()

    return app
