from app import create_app, db
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario

app = create_app()
app.app_context().push()

repositorio = RepositorioExpedienteSQL(db.session)
servicio = ServicioGestionExpedientes(repositorio)

usuario = Usuario(id=1, nombre="Fiscal Juan", correo="juan@example.com", rol=RolUsuario.FISCAL)

servicio.crear_expediente("Cliente de Prueba", usuario)

expedientes = servicio.obtener_expedientes_de_usuario(usuario)
for exp in expedientes:
    print(f"Expediente ID: {exp.id}, Cliente: {exp.cliente}, Estado: {exp.estado}")
    if exp.fiscal:
            print(f"Fiscal: {exp.fiscal.nombre}, Correo: {exp.fiscal.correo}, Rol: {exp.fiscal.rol}")
    if exp.asistente:
            print(f"Asistente: {exp.asistente.nombre}, Correo: {exp.asistente.correo}, Rol: {exp.asistente.rol}")

