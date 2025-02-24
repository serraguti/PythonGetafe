import oracledb

print("Buscador plantilla por turno")
print("Introduzca un Turno (T, M, N)")
data = input()
sql = "select APELLIDO, FUNCION from PLANTILLA where hospital_cod=" + data 
print(sql)
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
cursor.execute(sql)
#RECORREMOS LOS DATOS DEL CURSOR
for apellido, funcion in cursor:
    print(apellido + ", Función: " + funcion)
cursor.close()
connection.close()
print("Fin de BBDD")