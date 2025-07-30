# prueba_gui.py

import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.dominio.usuario import Usuario
from app.dominio.Rol_Usuario import RolUsuario
from app.dominio.expediente import Expediente
from app.infraestructura.repositorio_ExpedienteSQL import RepositorioExpedienteSQL
from app.aplicacion.servicio_Gestion_Expedientes import ServicioGestionExpedientes
from app import create_app

app = create_app()
DATABASE_URL = "sqlite:///expedientes.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
sesion = Session()

usuario_prueba = Usuario(id=1, nombre="Juan Fiscal", correo="juan.fiscal@hotmail.com", rol=RolUsuario.FISCAL)

repositorio = RepositorioExpedienteSQL(sesion)
servicio = ServicioGestionExpedientes(repositorio)
with app.app_context():
    expedientes = servicio.obtener_expedientes_de_usuario(usuario_prueba)

ventana = tk.Tk()
ventana.title("Expedientes del Usuario")

columnas = ("ID", "Cliente", "Estado")

tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150)

# Insertar expedientes en la tabla
for exp in expedientes:
    tabla.insert("", tk.END, values=(exp.id, exp.cliente, exp.estado))

tabla.pack(padx=20, pady=20, fill="both", expand=True)

ventana.mainloop()