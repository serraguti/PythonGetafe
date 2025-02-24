import oracledb
print("Insert hospitales BBDD")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca ID hospital")
idhospital = input()
print("Nombre de hospital")
nombre = input()
print("Dirección")
direccion = input()
print("Teléfono")
telefono = input()
print("Camas")
camas = input()

#insert into HOSPITAL values (11,'name','dir','tlf',camas)
sqlinsert = f"insert into HOSPITAL values ({idhospital},'{nombre}','{direccion}','{telefono}',{camas})"
print(sqlinsert)
cursor = connection.cursor()
cursor.execute(sqlinsert)
print(f"Filas insertadas: {cursor.rowcount}")
cursor.close()
sqlselect = "select * from HOSPITAL"
cursor = connection.cursor()
cursor.execute(sqlselect)
for row in cursor:
    print(row)
cursor.close()
connection.close()
print("Fin de programa")