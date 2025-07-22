from app import db
from app.dominio.Rol_Usuario import RolUsuario
from app.dominio.usuario import Usuario

class UsuarioModelo(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.Enum(RolUsuario), nullable=False)

def usuario_modelo_a_entidad(usuario_modelo: UsuarioModelo) -> Usuario:
    return Usuario(
        id=usuario_modelo.id,
        nombre=usuario_modelo.nombre,
        correo=usuario_modelo.correo,
        rol=RolUsuario(usuario_modelo.rol)
    )

def entidad_a_usuario_modelo(usuario: Usuario) -> UsuarioModelo:
    return UsuarioModelo(
        id=usuario.id,
        nombre=usuario.nombre,
        correo=usuario.correo,
        rol=usuario.rol.value
    )
