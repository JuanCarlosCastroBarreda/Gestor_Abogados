from app.dominio.usuario import Usuario


class ServicioGestionExpedientes:
    def __init__(self):
        pass

    def crearExpediente(self, cliente, usuario):
        pass

    def asignarExpediente(self, expediente, usuario):
        pass

    def cambiarEstadoExpediente(self, id, nuevoEstado):
        pass

    def agregarDocumentoAExpediente(self, idExpediente, documento):
        pass

    def obtenerExpedientesDeUsuario(self, usuario):
        pass
