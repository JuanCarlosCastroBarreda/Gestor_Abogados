from flask import Flask, render_template
from app import create_app, db
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL

app = create_app()

@app.route("/")
def inicio():
    usuario_prueba = Usuario(id=1, nombre="Juan Fiscal", correo="juan.fiscal@hotmail.com", rol=RolUsuario.FISCAL)
    servicio = ServicioGestionExpedientes(RepositorioExpedienteSQL(db.session))
    expedientes = servicio.obtener_expedientes_de_usuario(usuario_prueba)
    return render_template("expedientes.html", expedientes=expedientes)

if __name__ == "__main__":
    app.run(debug=True)
