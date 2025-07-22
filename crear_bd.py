from app import create_app, db
from sqlalchemy import inspect
from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario
from app.infraestructura.usuario_sql import UsuarioModelo, entidad_a_usuario_modelo

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos creada correctamente.")

    # Crear un usuario de prueba
    nuevo_usuario = Usuario(id=1, nombre="Juan Fiscal", correo="juan@fiscal.com", rol=RolUsuario.FISCAL)
    usuario_modelo = entidad_a_usuario_modelo(nuevo_usuario)

    # Guardar en la base de datos
    db.session.add(usuario_modelo)
    db.session.commit()
    print("Usuario insertado.")

    # Mostrar tablas
    inspector = inspect(db.engine)
    print(inspector.get_table_names())
