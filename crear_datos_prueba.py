from app import create_app, db
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario

app = create_app()

with app.app_context():
    db.create_all()
    
    repositorio = RepositorioExpedienteSQL()
    servicio = ServicioGestionExpedientes(repositorio)

    usuario = Usuario(id=1, nombre="Juan", correo="juan@correo.com", rol=RolUsuario.FISCAL)
    servicio.crear_expediente("Cliente Prueba", usuario)
