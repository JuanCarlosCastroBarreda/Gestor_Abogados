from app import db
from app.dominio.documento import Documento
from app.infraestructura.usuario_sql import UsuarioModelo
from app.dominio.Rol_Usuario import RolUsuario

class Expediente(db.Model):
    __tablename__ = 'expedientes'

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    fiscal_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    asistente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)

    fiscal = db.relationship('UsuarioModelo', foreign_keys=[fiscal_id])
    asistente = db.relationship('UsuarioModelo', foreign_keys=[asistente_id])

    documentos = db.relationship('Documento', backref='expediente', lazy=True)
