from conexion import Conexion


class ReporteInasistenciasDAO:

    def obtener_inasistencias(self, fecha):

        conexion_db = Conexion().conectar()

        if conexion_db is None:
            return []

        cursor = conexion_db.cursor()

        sql = """
        SELECT
            u.id_usuario,
            u.nombre
        FROM usuarios u
        WHERE u.rol = 'USUARIO'
        AND NOT EXISTS (
            SELECT 1
            FROM asistencias a
            WHERE a.id_usuario = u.id_usuario
            AND a.fecha = %s
            AND a.accion IN ('ENTRADA', 'SALIDA')
        )
        ORDER BY u.id_usuario
        """

        cursor.execute(
            sql,
            (fecha,)
        )

        resultados = cursor.fetchall()

        cursor.close()
        conexion_db.close()

        return resultados