#!/usr/bin/python
# -*- coding: utf-8 -*-

# app/infraestructura/repositorio_expediente_sql.py

from app.dominio.expediente import Expediente
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Protocol, Optional
import logging

logger = logging.getLogger(__name__)

# Principio de Segregación de Interfaces (ISP)
class IRepositorioExpediente(Protocol):
    def guardar_expediente(self, expediente: Expediente) -> None: ...
    def listar_expedientes(self) -> list[Expediente]: ...
    def buscar_expediente_por_id(self, expediente_id: int) -> Optional[Expediente]: ...
    def eliminar_expediente_por_id(self, expediente_id: int) -> None: ...
    def actualizar_expediente(self, expediente_id: int, datos_actualizados: dict) -> None: ...

# Principio de Responsabilidad Única (SRP)
class RepositorioExpedienteSQL(IRepositorioExpediente):
    def __init__(self, sesion: Session):
        self.sesion = sesion

    def guardar_expediente(self, expediente: Expediente) -> None:
        self._ejecutar_transaccion(lambda: self.sesion.add(expediente))

    def listar_expedientes(self) -> list[Expediente]:
        return self.sesion.query(Expediente).all()

    def buscar_expediente_por_id(self, expediente_id: int) -> Optional[Expediente]:
        return self.sesion.query(Expediente).filter(Expediente.id == expediente_id).first()

    def eliminar_expediente_por_id(self, expediente_id: int) -> None:
        def eliminar():
            expediente = self.buscar_expediente_por_id(expediente_id)
            if expediente:
                self.sesion.delete(expediente)
            else:
                logger.warning(f"No se encontró el expediente con ID {expediente_id}")
        self._ejecutar_transaccion(eliminar)

    def actualizar_expediente(self, expediente_id: int, datos_actualizados: dict) -> None:
        def actualizar():
            expediente = self.buscar_expediente_por_id(expediente_id)
            if expediente:
                for campo, valor in datos_actualizados.items():
                    setattr(expediente, campo, valor)
            else:
                logger.warning(f"No se encontró el expediente con ID {expediente_id}")
        self._ejecutar_transaccion(actualizar)

    # Principio de Abierto/Cerrado (OCP) → método genérico para ejecutar transacciones
    def _ejecutar_transaccion(self, operacion: callable) -> None:
        try:
            operacion()
            self.sesion.commit()
        except SQLAlchemyError as error:
            self.sesion.rollback()
            logger.error(f"Error en la transacción: {error}")
