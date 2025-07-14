#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Optional
from app.dominio.expediente import Expediente

class IExpedienteRepositorio(ABC):
    """
    Interfaz abstracta para definir operaciones del repositorio de Expediente.
    """

    @abstractmethod
    def obtener_por_id(self, expediente_id: int) -> Optional[Expediente]:
        pass

    @abstractmethod
    def listar_todos(self) -> List[Expediente]:
        pass

    @abstractmethod
    def guardar(self, expediente: Expediente) -> None:
        pass

    @abstractmethod
    def eliminar(self, expediente_id: int) -> None:
        pass
