import oracledb
print("Insertar departamentos")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

#PEDIMOS LOS DATOS AL USUARIO
print("Introduzca un Id departamento")
iddept = input()
print("Introduzca nombre")
nombre = input()
print("Introduzca localidad")
localidad = input()
#insert into DEPT values (99,'A','A')
sqlinsert = "insert into DEPT values (" + iddept + ",'" + nombre + "','" + localidad + "')"
print(sqlinsert)
cursor = connection.cursor()
cursor.execute(sqlinsert)
print("Departamentos insertados: " + str(cursor.rowcount))
cursor.close()
cursor = connection.cursor()
sqlselect = "select * from DEPT"
cursor.execute(sqlselect)
for row in cursor:
    print(row)
cursor.close()
connection.close()
print("Fin de programa")