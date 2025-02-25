import oracledb

class ConexionOracleEnfermos:
    #EN EL INICIO DE LA CLASE DEBEMOS CREAR
    #UN OBJETO connection PARA UTILIZARLO EN 
    #TODOS LOS METODOS (__init__)
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def eliminarEnfermo(self, inscripcion):
        cursor = self.connection.cursor()
        sql = "delete from ENFERMO where INSCRIPCION=:p1"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        cursor.close()
        return registros