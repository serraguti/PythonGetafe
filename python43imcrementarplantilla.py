import oracledb

print("Incrementar salario Plantilla/Hospital")
print("Introduzca ID de hospital")
idhospital = int(input())
print("Introduzca incremento salarial")
incremento = int(input())
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

sqlupdate = "update PLANTILLA set SALARIO=SALARIO + :p1 where HOSPITAL_COD=:p2"

cursor = connection.cursor()
cursor.execute(sqlupdate, (incremento, idhospital))
registros = cursor.rowcount
print(f"Registros modificados: {registros}")
connection.commit()
cursor.close()
sqlselect = "select APELLIDO, FUNCION, SALARIO from PLANTILLA where HOSPITAL_COD=:p1"
cursor = connection.cursor()
cursor.execute(sqlselect, (idhospital,))
for ape, fun, sal in cursor:
    print(f"Apellido: {ape}, Función: {fun}, Salario: {sal}")
cursor.close()
connection.close()
print("Fin de programa")