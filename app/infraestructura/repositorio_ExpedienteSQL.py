#!/usr/bin/python
# -*- coding: utf-8 -*-

# app/infraestructura/repositorio_expediente_sql.py

from app.dominio.expediente import Expediente
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class RepositorioExpedienteSQL:
    def __init__(self, sesion: Session):
        self.sesion = sesion

    def guardar_expediente(self, expediente: Expediente) -> None:
        try:
            self.sesion.add(expediente)
            self.sesion.commit()
        except SQLAlchemyError as error:
            self.sesion.rollback()
            print(f"No se pudo guardar el expediente: {error}")

    def listar_expedientes(self) -> list[Expediente]:
        return self.sesion.query(Expediente).all()

    def buscar_expediente_por_id(self, expediente_id: int) -> Expediente | None:
        return self.sesion.query(Expediente).filter(Expediente.id == expediente_id).first()

    def eliminar_expediente_por_id(self, expediente_id: int) -> None:
        try:
            expediente = self.buscar_expediente_por_id(expediente_id)
            if expediente:
                self.sesion.delete(expediente)
                self.sesion.commit()
            else:
                print(f"No se encontró el expediente con ID {expediente_id}")
        except SQLAlchemyError as error:
            self.sesion.rollback()
            print(f"No se pudo eliminar el expediente: {error}")

    def actualizar_expediente(self, expediente_id: int, datos_actualizados: dict) -> None:
        try:
            expediente = self.buscar_expediente_por_id(expediente_id)
            if expediente:
                for campo, valor in datos_actualizados.items():
                    setattr(expediente, campo, valor)
                self.sesion.commit()
            else:
                print(f"No se encontró el expediente con ID {expediente_id}")
        except SQLAlchemyError as error:
            self.sesion.rollback()
            print(f"No se pudo actualizar el expediente: {error}")