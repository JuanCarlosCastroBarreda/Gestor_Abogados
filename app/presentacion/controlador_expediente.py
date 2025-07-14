from flask import Blueprint, request, jsonify
from app.dominio.expediente import Expediente
from app import db

expediente_bp = Blueprint('expediente_bp', __name__)

@expediente_bp.route('/expedientes', methods=['POST'])
def crear_expediente():
    data = request.json
    nuevo = Expediente(
        cliente=data['cliente'],
        fecha=data['fecha'],
        estado=data['estado']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Expediente creado'}), 201
