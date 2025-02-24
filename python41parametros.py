import oracledb
print("Ejemplo de parámetros Oracle")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Introduzca número de departamento")
iddept = int(input())
sql = "select * from EMP where DEPT_NO=:param1"
print(sql)
cursor = connection.cursor()
cursor.execute(sql, (iddept,))
for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Departamento: {row[7]}")
cursor.close()
connection.close()
print("Fin de programa")









import oracledb
print("Ejemplo de parámetros Oracle")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Introduzca número de departamento")
iddept = input()
sql = "select * from EMP where DEPT_NO=:param1"
print(sql)
cursor = connection.cursor()
cursor.execute(sql, (iddept,))
for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Departamento: {row[7]}")
cursor.close()
connection.close()
print("Fin de programa")