#!/usr/bin/python
# -*- coding: utf-8 -*-

# app/infraestructura/repositorio_expediente_sql.py

from app.dominio.expediente import Expediente
from app.dominio.i_Expediente_Repositorio import IExpedienteRepositorio
from app import db

class RepositorioExpedienteSQL(IExpedienteRepositorio):
    def guardar(self, expediente: Expediente) -> None:
        db.session.add(expediente)
        db.session.commit()

    def obtener_por_id(self, id: int) -> Expediente:
        return Expediente.query.get(id)

    def listar_todos(self) -> list[Expediente]:
        return Expediente.query.all()

    def eliminar(self, id: int) -> None:
        expediente = Expediente.query.get(id)
        if expediente:
            db.session.delete(expediente)
            db.session.commit()

    def actualizar_estado(self, id: int, nuevo_estado: str) -> None:
        expediente = Expediente.query.get(id)
        if expediente:
            expediente.estado = nuevo_estado
            db.session.commit()

    def obtener_por_usuario(self, usuario) -> list[Expediente]:
        return Expediente.query.filter(
            (Expediente.fiscal_id == usuario.id) |
            (Expediente.asistente_id == usuario.id)
        ).all()

