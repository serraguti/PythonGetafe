#importamos la librería de Python Oracle
import oracledb

#tenemos un objeto connection(user, password, server)

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Conectados!!!")
# LAS CONSULTAS NO LLEVAN ;
sql = "select * from DEPT"

# CREAMOS UN CURSOR PARA REALIZAR LA CONSULTA
cursor = connection.cursor()
#LA CONSULTA SE EJECUTA Y RECUPERA LOS DATOS A LA VEZ
#AL APLICAR EL METODO execute(sql)
cursor.execute(sql)

#UNA VEZ QUE TENEMOS LOS DATOS EN EL CURSOR, DEBEMOS EXTRAERLOS
#PARA RECUPERAR LOS DATOS
#TENEMOS UN METODO LLAMADO fetchone() QUE NOS DEVUELVE UNA FILA
#CADA VEZ QUE EJECUTEMOS fetchone() AVANZA UNA FILA
row = cursor.fetchone()
#PINTAMOS LA FILA 1
print(row)
row = cursor.fetchone()
#PINTAMOS LA FILA 2
print(row)
row = cursor.fetchone()
#PINTAMOS LA FILA 3
print(row)
#PINTAMOS LA FILA 4
row = cursor.fetchone()
print(row)
#PINTAMOS LA FILA ????
row = cursor.fetchone()
print(row)
#POR NORMA, SIEMPRE DEBEMOS LIBERAR LOS RECURSOS DE BBDD
#CERRAR TODO
cursor.close()
connection.close()
print("Fin de BBDD")