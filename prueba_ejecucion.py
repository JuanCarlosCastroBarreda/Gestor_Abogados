from app import create_app, db
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario

# Crear app y contexto
app = create_app()
app.app_context().push()

# Crear repositorio y servicio
repositorio = RepositorioExpedienteSQL()
servicio = ServicioGestionExpedientes(repositorio)

# Crear usuario (simulado)
usuario = Usuario(id=1, nombre="Fiscal Juan", correo="juan@example.com", rol=RolUsuario.FISCAL)

# Probar creación de expediente
servicio.crear_expediente("Cliente de Prueba", usuario)

# Mostrar los expedientes existentes
expedientes = servicio.obtener_expedientes_de_usuario(usuario)
for exp in expedientes:
    print(f"Expediente ID: {exp.id}, Cliente: {exp.cliente}, Estado: {exp.estado}")
