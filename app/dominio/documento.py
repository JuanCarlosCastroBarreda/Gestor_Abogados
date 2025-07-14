# app/dominio/documento.py

from app import db

class Documento(db.Model):
    """
    Modelo que representa un documento asociado a un expediente.
    """
    __tablename__ = 'documentos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=True)
    expediente_id = db.Column(db.Integer, db.ForeignKey('expedientes.id'), nullable=False)

    def __repr__(self) -> str:
        return f"<Documento {self.nombre} (Tipo: {self.tipo})>"
