import tkinter as tk

from tkinter import messagebox

from usuario_dao import UsuarioDAO


class CrearUsuarioView:

    def __init__(self, ventana_padre):

        self.ventana_padre = ventana_padre

        self.dao = UsuarioDAO()

        self.ventana = tk.Toplevel()

        self.ventana.title("Crear Usuario")
        self.ventana.geometry("400x350")


        titulo = tk.Label(
            self.ventana,
            text="Crear Usuario",
            font=("Arial", 18)
        )

        titulo.pack(pady=20)


        # NOMBRE
        tk.Label(
            self.ventana,
            text="Nombre"
        ).pack()

        self.txt_nombre = tk.Entry(
            self.ventana,
            width=30
        )

        self.txt_nombre.pack(pady=5)


        # CORREO
        tk.Label(
            self.ventana,
            text="Correo"
        ).pack()

        self.txt_correo = tk.Entry(
            self.ventana,
            width=30
        )

        self.txt_correo.pack(pady=5)


        # CONTRASEÑA
        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()

        self.txt_contrasena = tk.Entry(
            self.ventana,
            width=30,
            show="*"
        )

        self.txt_contrasena.pack(pady=5)


        # BOTÓN CREAR
        boton_crear = tk.Button(
            self.ventana,
            text="Crear Usuario",
            width=20,
            command=self.crear_usuario
        )

        boton_crear.pack(pady=20)


        # BOTÓN CERRAR
        boton_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            width=20,
            command=self.ventana.destroy
        )

        boton_cerrar.pack()


    def crear_usuario(self):

        nombre = self.txt_nombre.get().strip()
        correo = self.txt_correo.get().strip()
        contrasena = self.txt_contrasena.get().strip()


        # VALIDAR CAMPOS VACÍOS
        if (
            nombre == ""
            or correo == ""
            or contrasena == ""
        ):

            messagebox.showwarning(
                "Crear Usuario",
                "Todos los campos son obligatorios."
            )

            return


        # VALIDAR CORREO
        if "@" not in correo:

            messagebox.showwarning(
                "Crear Usuario",
                "Debe ingresar un correo válido."
            )

            return


        # VALIDAR CORREO DUPLICADO
        if self.dao.correo_existe(correo):

            messagebox.showwarning(
                "Crear Usuario",
                "El correo ingresado ya está registrado."
            )

            return


        # CREAR USUARIO
        resultado = self.dao.crear_usuario(
            nombre,
            correo,
            contrasena
        )


        if resultado:

            messagebox.showinfo(
                "Crear Usuario",
                "Usuario creado correctamente."
            )

            self.limpiar_campos()


    def limpiar_campos(self):

        self.txt_nombre.delete(
            0,
            tk.END
        )

        self.txt_correo.delete(
            0,
            tk.END
        )

        self.txt_contrasena.delete(
            0,
            tk.END
        )

        self.txt_nombre.focus()