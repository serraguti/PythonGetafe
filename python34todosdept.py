import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

sql = "select * from DEPT"
cursor = connection.cursor()
cursor.execute(sql)
for numero, nombre, localidad in cursor:
    print(str(numero) + ": " + nombre + ", " + localidad)

#PARA RECORRER UN CURSOR SE UTILIZAN BUCLES for
#for row in cursor:
    #print(row)
    # SI DESEAMOS EXTRAER DATOS DE ALGUNA COLUMNA
    # PODEMOS REALIZARLO POR EL INDICE
    #print(row[2])
    # TAMBIEN PODEMOS RECUPERAR LOS DATOS
    # POR NOMBRE DE COLUMNA.  PERO ESTO
    # SOLAMENTE ES COMPATIBLE CON ALGUNAS BBDD
    #nombre = row.DNOMBRE
    #print(nombre)
# EL CURSOR SOLAMENTE SE PUEDE LEER UNA VEZ
# SI DESEAMOS LEER DE NUEVO, DEBEMOS EJECUTAR DE NUEVO
fila = cursor.fetchone()
print(fila)
cursor.close()
connection.close()
print("Fin de BBDD")
