import mysql.connector


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "control_asistencia"

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            return conexion

        except mysql.connector.Error as error:
            print("Error al conectar con MySQL:", error)
            return None