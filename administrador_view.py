import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from reporte_atrasos_dao import ReporteAtrasosDAO
from reporte_salidas_dao import ReporteSalidasDAO
from reporte_inasistencias_dao import ReporteInasistenciasDAO

from crear_usuario_view import CrearUsuarioView
from modificar_usuario_view import ModificarUsuarioView


class AdministradorView:

    def __init__(
        self,
        root_principal,
        usuario,
        login_view
    ):

        self.root_principal = root_principal
        self.usuario = usuario
        self.login_view = login_view

        self.atrasos_dao = ReporteAtrasosDAO()
        self.salidas_dao = ReporteSalidasDAO()
        self.inasistencias_dao = ReporteInasistenciasDAO()

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Panel Administrador"
        )

        self.ventana.geometry(
            "650x580"
        )


        titulo = tk.Label(
            self.ventana,
            text=f"Administrador: {usuario.nombre}",
            font=("Arial", 16)
        )

        titulo.pack(
            pady=20
        )


        # CREAR USUARIO
        boton_crear_usuario = tk.Button(
            self.ventana,
            text="Crear Usuario",
            width=30,
            command=self.abrir_crear_usuario
        )

        boton_crear_usuario.pack(
            pady=5
        )


        # MODIFICAR USUARIO
        boton_modificar_usuario = tk.Button(
            self.ventana,
            text="Modificar Usuario",
            width=30,
            command=self.abrir_modificar_usuario
        )

        boton_modificar_usuario.pack(
            pady=5
        )


        # REPORTE DE ATRASOS
        boton_reporte = tk.Button(
            self.ventana,
            text="Reporte de Entradas Atrasadas",
            width=30,
            command=self.mostrar_reporte
        )

        boton_reporte.pack(
            pady=5
        )


        # REPORTE DE SALIDAS
        boton_salidas = tk.Button(
            self.ventana,
            text="Reporte de Salidas Anticipadas",
            width=30,
            command=self.mostrar_salidas_anticipadas
        )

        boton_salidas.pack(
            pady=5
        )


        # FECHA PARA INASISTENCIAS
        frame_fecha = tk.Frame(
            self.ventana
        )

        frame_fecha.pack(
            pady=10
        )


        etiqueta_fecha = tk.Label(
            frame_fecha,
            text="Fecha:"
        )

        etiqueta_fecha.pack(
            side=tk.LEFT
        )


        self.txt_fecha = tk.Entry(
            frame_fecha,
            width=12
        )

        self.txt_fecha.pack(
            side=tk.LEFT,
            padx=5
        )


        boton_inasistencias = tk.Button(
            frame_fecha,
            text="Reporte de Inasistencias",
            command=self.mostrar_inasistencias
        )

        boton_inasistencias.pack(
            side=tk.LEFT
        )


        # TABLA
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "id",
                "nombre",
                "fecha",
                "hora"
            ),
            show="headings"
        )


        self.tabla.heading(
            "id",
            text="ID Usuario"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.heading(
            "hora",
            text="Hora"
        )


        self.tabla.column(
            "id",
            width=80
        )

        self.tabla.column(
            "nombre",
            width=180
        )

        self.tabla.column(
            "fecha",
            width=120
        )

        self.tabla.column(
            "hora",
            width=120
        )


        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        # CERRAR SESIÓN
        boton_cerrar = tk.Button(
            self.ventana,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        )

        boton_cerrar.pack(
            pady=10
        )


    def abrir_crear_usuario(self):

        CrearUsuarioView(
            self.ventana
        )


    def abrir_modificar_usuario(self):

        ModificarUsuarioView(
            self.ventana
        )


    def mostrar_reporte(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)


        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.heading(
            "hora",
            text="Hora Entrada"
        )


        atrasos = (
            self.atrasos_dao.obtener_atrasos()
        )


        for atraso in atrasos:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    atraso[0],
                    atraso[1],
                    atraso[2],
                    atraso[3]
                )
            )


    def mostrar_salidas_anticipadas(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)


        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.heading(
            "hora",
            text="Hora Salida"
        )


        salidas = (
            self.salidas_dao.obtener_salidas_anticipadas()
        )


        for salida in salidas:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    salida[0],
                    salida[1],
                    salida[2],
                    salida[3]
                )
            )


    def mostrar_inasistencias(self):

        fecha = (
            self.txt_fecha.get()
        )


        if fecha == "":

            messagebox.showwarning(
                "Fecha",
                "Debe ingresar una fecha."
            )

            return


        try:

            datetime.strptime(
                fecha,
                "%Y-%m-%d"
            )

        except ValueError:

            messagebox.showwarning(
                "Fecha",
                "La fecha debe tener formato AAAA-MM-DD."
            )

            return


        for fila in self.tabla.get_children():
            self.tabla.delete(fila)


        self.tabla.heading(
            "id",
            text="ID Usuario"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.heading(
            "hora",
            text="Estado"
        )


        inasistencias = (
            self.inasistencias_dao.obtener_inasistencias(
                fecha
            )
        )


        for inasistencia in inasistencias:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    inasistencia[0],
                    inasistencia[1],
                    fecha,
                    "INASISTENTE"
                )
            )


    def cerrar_sesion(self):

        self.ventana.destroy()

        self.login_view.limpiar_campos()

        self.root_principal.deiconify()