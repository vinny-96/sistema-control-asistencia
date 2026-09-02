from conexion import Conexion


class ReporteSalidasDAO:

    def obtener_salidas_anticipadas(self):

        conexion_db = Conexion().conectar()

        if conexion_db is None:
            return []

        cursor = conexion_db.cursor()

        sql = """
        SELECT
            a.id_usuario,
            u.nombre,
            a.fecha,
            a.hora
        FROM asistencias a
        INNER JOIN usuarios u
            ON a.id_usuario = u.id_usuario
        WHERE a.accion = 'SALIDA'
        AND a.hora < '17:30:00'
        ORDER BY a.fecha DESC, a.hora ASC
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conexion_db.close()

        return resultados