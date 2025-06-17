from enum import Enum
from app.dominio.expediente import Expediente

class RolUsuario(Enum):
    FISCAL = "FISCAL"
    ASISTENTE = "ASISTENTE"
    ADMIN = "ADMIN"

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

    def puede_acceder(self, expediente: Expediente) -> bool:
        # Esto depende de tu lógica. Aquí va un ejemplo:
        if self.rol == RolUsuario.ADMIN:
            return True
        if self.rol == RolUsuario.FISCAL and expediente.fiscal_id == self.id:
            return True
        if self.rol == RolUsuario.ASISTENTE and expediente.asistente_id == self.id:
            return True
        return False

    def __repr__(self):
        return f"<Usuario {self.nombre} - {self.rol.value}>"
