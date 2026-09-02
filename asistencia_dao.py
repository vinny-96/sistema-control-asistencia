from conexion import Conexion
from datetime import datetime


class AsistenciaDAO:

    def obtener_ultima_accion(self, id_usuario):

        conexion_db = Conexion().conectar()

        if conexion_db is None:
            return None

        cursor = conexion_db.cursor()

        sql = """
        SELECT accion
        FROM asistencias
        WHERE id_usuario = %s
        ORDER BY id_asistencia DESC
        LIMIT 1
        """

        cursor.execute(sql, (id_usuario,))

        resultado = cursor.fetchone()

        cursor.close()
        conexion_db.close()

        if resultado:
            return resultado[0]

        return None


    def registrar(self, id_usuario, accion):

        conexion_db = Conexion().conectar()

        if conexion_db is None:
            return False

        cursor = conexion_db.cursor()

        ahora = datetime.now()

        sql = """
        INSERT INTO asistencias
        (id_usuario, accion, fecha, hora)
        VALUES (%s, %s, %s, %s)
        """

        datos = (
            id_usuario,
            accion,
            ahora.date(),
            ahora.time()
        )

        cursor.execute(sql, datos)

        conexion_db.commit()

        cursor.close()
        conexion_db.close()

        return True