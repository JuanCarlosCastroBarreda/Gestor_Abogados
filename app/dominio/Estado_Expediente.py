#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class EstadoExpediente(Enum):
    EN_CURSO = 1
    COMPLETADO = 2
    ARCHIVADO = 3
