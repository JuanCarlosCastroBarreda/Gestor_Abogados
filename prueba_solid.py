from app import db, create_app
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario
from app.infraestructura.usuario_sql import (
    entidad_a_usuario_modelo,
    usuario_modelo_a_entidad,
    UsuarioModelo
)

def prueba_usuario_sql():
    usuario = Usuario(id=None, nombre="Juan", correo="juan@example.com", rol=RolUsuario.FISCAL)

    modelo = entidad_a_usuario_modelo(usuario)

    db.session.add(modelo)
    db.session.commit()

    recuperado = UsuarioModelo.query.filter_by(correo="juan@example.com").first()

    usuario_recuperado = usuario_modelo_a_entidad(recuperado)

    print(usuario_recuperado)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        prueba_usuario_sql()
