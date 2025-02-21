import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Conectado a BBDD")
print("Introduzca número de departamento")
data = input()
cursor = connection.cursor()
sql = "select * from DEPT where DEPT_NO=" + data
cursor.execute(sql)
#COMO ESTAMOS BUSCANDO POR PK, SOLAMENTE NOS PUEDE 
#DEVOLVER UNA FILA
row = cursor.fetchone()
#DEBEMOS COMPROBAR SI FILA TIENE CONTENIDO/ALGO
if (not row):
    print("No existe el departamento")
else:
    #DIBUJAMOS LOS DATOS
    nombre = row[1]
    localidad = row[2]
    print(nombre + ", " + localidad)
cursor.close()
connection.close()
print("Fin de bbdd")