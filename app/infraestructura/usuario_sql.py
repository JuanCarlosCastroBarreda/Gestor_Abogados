from app import db
from app.dominio.Rol_Usuario import RolUsuario
from app.dominio.usuario import Usuario

# Principio SRP: Esta clase solo define el modelo ORM para la tabla 'usuarios'
class UsuarioModelo(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.Enum(RolUsuario), nullable=False)

# Principio SRP: Esta función convierte un modelo ORM en una entidad de dominio
def usuario_modelo_a_entidad(usuario_modelo: UsuarioModelo) -> Usuario:
    return Usuario(
        id=usuario_modelo.id,
        nombre=usuario_modelo.nombre,
        correo=usuario_modelo.correo,
        rol=usuario_modelo.rol  # Ya es un RolUsuario
    )

# Principio SRP: Esta función convierte una entidad de dominio en un modelo ORM
def entidad_a_usuario_modelo(usuario: Usuario) -> UsuarioModelo:
    modelo = UsuarioModelo(
        nombre=usuario.nombre,
        correo=usuario.correo,
        rol=usuario.rol
    )
    # Solo asignamos ID si ya existe (para evitar errores al insertar nuevos)
    if usuario.id is not None:
        modelo.id = usuario.id
    return modelo
