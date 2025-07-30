# app/aplicacion/servicio_gestion_expedientes.py
from app.dominio.usuario import Usuario
from app.dominio.expediente import Expediente
from app.dominio.documento import Documento
from app.dominio.i_Expediente_Repositorio import IExpedienteRepositorio

class ServicioGestionExpedientes:
    def __init__(self, repositorio_expedientes: IExpedienteRepositorio):
       self.repositorio_expedientes = repositorio_expedientes

    def crear_expediente(self, cliente: str, usuario: Usuario):
       expediente = Expediente(cliente=cliente, estado="Nuevo", fiscal_id=usuario.id)
       self.repositorio_expedientes.guardar(expediente)

    def asignar_expediente(self, expediente_id: int, usuario: Usuario):
       expediente = self.repositorio_expedientes.obtener_por_id(expediente_id)
       if usuario.rol.value == "FISCAL":
           expediente.fiscal_id = usuario.id
       elif usuario.rol.value == "ASISTENTE":
           expediente.asistente_id = usuario.id
       self.repositorio_expedientes.guardar(expediente)

    def cambiar_estado_expediente(self, expediente_id: int, nuevo_estado: str):
       expediente = self.repositorio_expedientes.obtener_por_id(expediente_id)
       expediente.estado = nuevo_estado
       self.repositorio_expedientes.guardar(expediente)

    def agregar_documento_a_expediente(self, expediente_id: int, documento: Documento):
       expediente = self.repositorio_expedientes.obtener_por_id(expediente_id)
       expediente.documentos.append(documento)
       self.repositorio_expedientes.guardar(expediente)

    def obtener_expedientes_de_usuario(self, usuario: Usuario):
       return self.repositorio_expedientes.obtener_por_usuario(usuario)