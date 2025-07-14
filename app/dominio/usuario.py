from app.dominio.Rol_Usuario import RolUsuario

class Usuario:
    def __init__(self, id: int, nombre: str, correo: str, rol: RolUsuario):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def es_fiscal(self) -> bool:
        return self.rol == RolUsuario.FISCAL

    def es_asistente(self) -> bool:
        return self.rol == RolUsuario.ASISTENTE

    def puede_acceder(self, expediente) -> bool:
        return expediente.asignado_a == self
