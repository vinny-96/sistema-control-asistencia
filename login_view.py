import tkinter as tk
from tkinter import messagebox

from usuario_dao import UsuarioDAO
from asistencia_view import AsistenciaView
from administrador_view import AdministradorView


class LoginView:

    def __init__(self, root):

        self.root = root

        self.root.title("Control de Asistencia")
        self.root.geometry("350x250")

        self.dao = UsuarioDAO()

        titulo = tk.Label(
            root,
            text="Inicio de Sesión",
            font=("Arial", 18)
        )

        titulo.pack(pady=20)

        tk.Label(
            root,
            text="Correo"
        ).pack()

        self.txt_correo = tk.Entry(
            root,
            width=30
        )

        self.txt_correo.pack(pady=5)

        tk.Label(
            root,
            text="Contraseña"
        ).pack()

        self.txt_contrasena = tk.Entry(
            root,
            width=30,
            show="*"
        )

        self.txt_contrasena.pack(pady=5)

        boton_login = tk.Button(
            root,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )

        boton_login.pack(pady=20)


    def iniciar_sesion(self):

        correo = self.txt_correo.get()
        contrasena = self.txt_contrasena.get()

        usuario = self.dao.iniciar_sesion(
            correo,
            contrasena
        )

        if usuario:

            messagebox.showinfo(
                "Inicio de sesión",
                "Inicio de sesión correcto"
            )

            self.root.withdraw()

            if usuario.rol == "ADMIN":

                AdministradorView(
                    self.root,
                    usuario,
                    self
                )

            else:

                AsistenciaView(
                    self.root,
                    usuario,
                    self
                )

        else:

            messagebox.showerror(
                "Error",
                "Correo o contraseña incorrectos"
            )


    def limpiar_campos(self):

        self.txt_correo.delete(
            0,
            tk.END
        )

        self.txt_contrasena.delete(
            0,
            tk.END
        )

        self.txt_correo.focus()