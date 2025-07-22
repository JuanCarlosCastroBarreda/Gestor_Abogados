from flask import jsonify

class ExpedientePresenter:
    @staticmethod
    def respuesta_exito(mensaje, status=200):
        return jsonify({'mensaje': mensaje}), status

    @staticmethod
    def respuesta_error(mensaje, status=400):
        return jsonify({'error': mensaje}), status