from flask import Blueprint, request, render_template
from app.dominio.expediente import Expediente
from app import db
from app.presentacion.presenter import ExpedientePresenter

expediente_bp = Blueprint('expediente_bp', __name__)

@expediente_bp.route('/expedientes', methods=['POST'])
def crear_expediente():
    data = request.get_json()
    if not data:
        return ExpedientePresenter.respuesta_error('Faltan datos JSON')
    cliente = data.get('cliente')
    estado = data.get('estado')
    if not cliente or not estado:
        return ExpedientePresenter.respuesta_error('Faltan campos obligatorios')
    try:
        nuevo = Expediente(cliente=cliente, estado=estado)
        db.session.add(nuevo)
        db.session.commit()
        return ExpedientePresenter.respuesta_exito('Expediente creado')
    except Exception as e:
        db.session.rollback()
        return ExpedientePresenter.respuesta_error(f'Error: {str(e)}', status=500)

@expediente_bp.route('/expedientes', methods=['GET'])
def listar_expedientes():
    try:
        expedientes = Expediente.query.all()
        resultado = [
            {'id': exp.id, 'cliente': exp.cliente, 'estado': exp.estado}
            for exp in expedientes
        ]
        return ExpedientePresenter.respuesta_exito(resultado, status=200)
    except Exception as e:
        return ExpedientePresenter.respuesta_error(f'Error: {str(e)}', status=500)

@expediente_bp.route('/expedientes/<int:expediente_id>', methods=['GET'])
def obtener_expediente(expediente_id):
    try:
        exp = Expediente.query.get_or_404(expediente_id)
        resultado = {'id': exp.id, 'cliente': exp.cliente, 'estado': exp.estado}
        return ExpedientePresenter.respuesta_exito(resultado, status=200)
    except Exception as e:
        return ExpedientePresenter.respuesta_error(f'Error: {str(e)}', status=500)

@expediente_bp.route('/expedientes/<int:expediente_id>', methods=['PUT'])
def actualizar_expediente(expediente_id):
    data = request.get_json()
    if not data:
        return ExpedientePresenter.respuesta_error('Faltan datos JSON')
    try:
        exp = Expediente.query.get_or_404(expediente_id)
        exp.cliente = data.get('cliente', exp.cliente)
        exp.estado = data.get('estado', exp.estado)
        db.session.commit()
        return ExpedientePresenter.respuesta_exito('Expediente actualizado')
    except Exception as e:
        db.session.rollback()
        return ExpedientePresenter.respuesta_error(f'Error: {str(e)}', status=500)

@expediente_bp.route('/expedientes/<int:expediente_id>', methods=['DELETE'])
def eliminar_expediente(expediente_id):
    try:
        exp = Expediente.query.get_or_404(expediente_id)
        db.session.delete(exp)
        db.session.commit()
        return ExpedientePresenter.respuesta_exito('Expediente eliminado')
    except Exception as e:
        db.session.rollback()
        return ExpedientePresenter.respuesta_error(f'Error: {str(e)}', status=500)

# Vistas HTML
@expediente_bp.route('/expedientes/vista', methods=['GET'])
def vista_expedientes():
    expedientes = Expediente.query.all()
    return render_template('expedientes.html', expedientes=expedientes)

@expediente_bp.route('/expedientes/vista/<int:expediente_id>', methods=['GET'])
def vista_detalle_expediente(expediente_id):
    expediente = Expediente.query.get_or_404(expediente_id)
    return render_template('detalle_expediente.html', expediente=expediente)
