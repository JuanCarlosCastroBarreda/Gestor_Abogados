
from app import create_app, db
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario
from app.dominio.expediente import Expediente
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL


app = create_app()

with app.app_context():
    db.create_all()

    db.session.query(Expediente).delete()

    db.session.commit()

    sesion = db.session
    repositorio = RepositorioExpedienteSQL(sesion)
    servicio = ServicioGestionExpedientes(repositorio)

    usuario = Usuario(id=1, nombre="Juan", correo="juan@correo.com", rol=RolUsuario.FISCAL)
    servicio.crear_expediente("Cliente Prueba", usuario)

    expedientes = db.session.query(Expediente).all()
    for exp in expedientes:
        print(f"Expediente ID: {exp.id}, Cliente: {exp.cliente}, Estado: {exp.estado}")
        if exp.fiscal:
            print(f"Fiscal: {exp.fiscal.nombre}, Correo: {exp.fiscal.correo}, Rol: {exp.fiscal.rol}")
        if exp.asistente:
            print(f"Asistente: {exp.asistente.nombre}, Correo: {exp.asistente.correo}, Rol: {exp.asistente.rol}")


