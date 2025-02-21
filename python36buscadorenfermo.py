import oracledb

print("Buscador de Enfermo")
print("Introduzca inscripción del Enfermo")
data = input()
sql = "select * from ENFERMO where INSCRIPCION=" + data;
#CONFIGURAMOS NUESTRAS CONEXIONES
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
cursor.execute(sql)
row = cursor.fetchone()
if (not row):
    print("No existe el enfermo con la inscripcion " + data)
else:
    apellido = row[1]
    direccion = row[2]
    print(apellido + ", Dirección: " + direccion)
cursor.close()
connection.close()
print("Fin de programa")