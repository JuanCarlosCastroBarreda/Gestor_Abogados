#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class EstadoExpediente(Enum):
    EN_CURSO = "EN_CURSO"
    COMPLETADO = "COMPLETADO"
    ARCHIVADO = "ARCHIVADO"
