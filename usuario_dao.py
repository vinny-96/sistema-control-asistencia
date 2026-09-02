from conexion import Conexion
from usuario import Usuario


class UsuarioDAO:

    def iniciar_sesion(self, correo, contrasena):

        conexion_db = Conexion().conectar()

        if conexion_db is None:
            return None

        cursor = conexion_db.cursor()

        sql = """
        SELECT id_usuario, nombre, correo, contrasena, rol
        FROM usuarios
        WHERE correo = %s AND contrasena = %s
        """

        cursor.execute(sql, (correo, contrasena))

        resultado = cursor.fetchone()

        cursor.close()
        conexion_db.close()

        if resultado:

            usuario = Usuario(
                resultado[0],
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[4]
            )

            return usuario

        return None
    