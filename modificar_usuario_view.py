import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from usuario_dao import UsuarioDAO


class ModificarUsuarioView:

    def __init__(
        self,
        ventana_padre
    ):

        self.ventana_padre = ventana_padre

        self.dao = UsuarioDAO()

        self.usuarios = []

        self.id_usuario_seleccionado = None

        self.ventana = tk.Toplevel(
            self.ventana_padre
        )

        self.ventana.title(
            "Modificar Usuario"
        )

        self.ventana.geometry(
            "450x450"
        )


        titulo = tk.Label(
            self.ventana,
            text="Modificar Usuario",
            font=("Arial", 18)
        )

        titulo.pack(
            pady=20
        )


        # SELECCIÓN DE USUARIO
        tk.Label(
            self.ventana,
            text="Seleccionar usuario"
        ).pack()


        self.combo_usuarios = ttk.Combobox(
            self.ventana,
            width=35,
            state="readonly"
        )

        self.combo_usuarios.pack(
            pady=5
        )

        self.combo_usuarios.bind(
            "<<ComboboxSelected>>",
            self.seleccionar_usuario
        )


        # NOMBRE
        tk.Label(
            self.ventana,
            text="Nombre"
        ).pack()


        self.txt_nombre = tk.Entry(
            self.ventana,
            width=35
        )

        self.txt_nombre.pack(
            pady=5
        )


        # CORREO
        tk.Label(
            self.ventana,
            text="Correo"
        ).pack()


        self.txt_correo = tk.Entry(
            self.ventana,
            width=35
        )

        self.txt_correo.pack(
            pady=5
        )


        # CONTRASEÑA
        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()


        self.txt_contrasena = tk.Entry(
            self.ventana,
            width=35,
            show="*"
        )

        self.txt_contrasena.pack(
            pady=5
        )


        # BOTÓN GUARDAR
        boton_modificar = tk.Button(
            self.ventana,
            text="Guardar Cambios",
            width=20,
            command=self.modificar_usuario
        )

        boton_modificar.pack(
            pady=20
        )


        # BOTÓN CERRAR
        boton_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            width=20,
            command=self.ventana.destroy
        )

        boton_cerrar.pack()


        self.cargar_usuarios()


    def cargar_usuarios(self):

        self.usuarios = (
            self.dao.obtener_usuarios()
        )

        lista = []

        for usuario in self.usuarios:

            texto = (
                f"{usuario[0]} - {usuario[1]}"
            )

            lista.append(texto)

        self.combo_usuarios[
            "values"
        ] = lista


    def seleccionar_usuario(
        self,
        event
    ):

        indice = (
            self.combo_usuarios.current()
        )

        if indice == -1:
            return

        usuario = self.usuarios[indice]

        self.id_usuario_seleccionado = (
            usuario[0]
        )


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


        self.txt_nombre.insert(
            0,
            usuario[1]
        )

        self.txt_correo.insert(
            0,
            usuario[2]
        )

        self.txt_contrasena.insert(
            0,
            usuario[3]
        )


    def modificar_usuario(self):

        if self.id_usuario_seleccionado is None:

            messagebox.showwarning(
                "Modificar Usuario",
                "Debe seleccionar un usuario."
            )

            return


        nombre = (
            self.txt_nombre.get().strip()
        )

        correo = (
            self.txt_correo.get().strip()
        )

        contrasena = (
            self.txt_contrasena.get().strip()
        )


        if (
            nombre == ""
            or correo == ""
            or contrasena == ""
        ):

            messagebox.showwarning(
                "Modificar Usuario",
                "Todos los campos son obligatorios."
            )

            return


        if "@" not in correo:

            messagebox.showwarning(
                "Modificar Usuario",
                "Debe ingresar un correo válido."
            )

            return


        if self.dao.correo_existe_otro_usuario(
            correo,
            self.id_usuario_seleccionado
        ):

            messagebox.showwarning(
                "Modificar Usuario",
                "El correo ya pertenece a otro usuario."
            )

            return


        resultado = (
            self.dao.actualizar_usuario(
                self.id_usuario_seleccionado,
                nombre,
                correo,
                contrasena
            )
        )


        if resultado:

            messagebox.showinfo(
                "Modificar Usuario",
                "Usuario modificado correctamente."
            )

            self.cargar_usuarios()

            self.combo_usuarios.set("")

            self.limpiar_campos()

            self.id_usuario_seleccionado = None


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