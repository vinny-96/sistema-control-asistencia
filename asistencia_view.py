import tkinter as tk
from tkinter import messagebox

from asistencia_dao import AsistenciaDAO


class AsistenciaView:

    def __init__(
        self,
        root_principal,
        usuario,
        login_view
    ):

        self.root_principal = root_principal
        self.usuario = usuario
        self.login_view = login_view

        self.dao = AsistenciaDAO()

        self.ventana = tk.Toplevel()

        self.ventana.title("Control de Asistencia")
        self.ventana.geometry("400x300")

        titulo = tk.Label(
            self.ventana,
            text=f"Bienvenido {usuario.nombre}",
            font=("Arial", 16)
        )

        titulo.pack(pady=30)

        self.lbl_estado = tk.Label(
            self.ventana,
            font=("Arial", 12)
        )

        self.lbl_estado.pack(pady=10)

        self.boton_accion = tk.Button(
            self.ventana,
            width=25,
            height=2
        )

        self.boton_accion.pack(pady=20)

        boton_cerrar = tk.Button(
            self.ventana,
            text="Cerrar sesión",
            width=20,
            command=self.cerrar_sesion
        )

        boton_cerrar.pack(pady=10)

        self.configurar_accion()


    def configurar_accion(self):

        ultima_accion = self.dao.obtener_ultima_accion(
            self.usuario.id_usuario
        )

        if ultima_accion == "ENTRADA":

            self.lbl_estado.config(
                text="Estado actual: DENTRO"
            )

            self.boton_accion.config(
                text="Marcar Salida",
                command=self.marcar_salida
            )

        else:

            self.lbl_estado.config(
                text="Estado actual: FUERA"
            )

            self.boton_accion.config(
                text="Marcar Entrada",
                command=self.marcar_entrada
            )


    def marcar_entrada(self):

        ultima_accion = self.dao.obtener_ultima_accion(
            self.usuario.id_usuario
        )

        if ultima_accion == "ENTRADA":

            messagebox.showwarning(
                "Entrada",
                "El usuario ya se encuentra dentro."
            )

            return

        resultado = self.dao.registrar(
            self.usuario.id_usuario,
            "ENTRADA"
        )

        if resultado:

            messagebox.showinfo(
                "Asistencia",
                "Entrada registrada correctamente."
            )

            self.cerrar_sesion()


    def marcar_salida(self):

        ultima_accion = self.dao.obtener_ultima_accion(
            self.usuario.id_usuario
        )

        if ultima_accion != "ENTRADA":

            messagebox.showwarning(
                "Salida",
                "El usuario no tiene una entrada activa."
            )

            return

        resultado = self.dao.registrar(
            self.usuario.id_usuario,
            "SALIDA"
        )

        if resultado:

            messagebox.showinfo(
                "Asistencia",
                "Salida registrada correctamente."
            )

            self.cerrar_sesion()


    def cerrar_sesion(self):

        self.ventana.destroy()

        self.login_view.limpiar_campos()

        self.root_principal.deiconify()