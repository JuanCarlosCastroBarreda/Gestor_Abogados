from app import db

class Expediente(db.Model):
    __tablename__ = 'expedientes'

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    fiscal_id = db.Column(db.Integer, nullable=True)
    asistente_id = db.Column(db.Integer, nullable=True)
    documentos = db.relationship('Documento', backref='expediente', lazy=True)
