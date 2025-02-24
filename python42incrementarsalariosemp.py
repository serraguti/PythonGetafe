import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Incrementar salario empleados")
print("Introduzca incremento")
incremento = int(input())
print("Introduzca el oficio a incrementar:")
oficio = input()
#CON CONSULTAS SQL SIEMPRE PARAM
sqlupdate = "update EMP set SALARIO = SALARIO + :p1 where OFICIO=:p2"
cursor = connection.cursor()
cursor.execute(sqlupdate, (incremento, oficio))
#CONSULTA DE ACCION, DEVUELVE REGISTROS AFECTADOS
registros = cursor.rowcount
#ALMACENAMOS EN BBDD
connection.commit()
#CERRAMOS CURSOR
cursor.close()
print(f"Empleados modificados: {registros}")
cursor = connection.cursor()
sqlselect  = "select APELLIDO, OFICIO, SALARIO from EMP where OFICIO=:p1"
cursor.execute(sqlselect,(oficio,))
for ape,ofi, sal in cursor:
    print(f"Apellido: {ape}, Oficio: {ofi}, Salario: {sal}")
cursor.close()
connection.close()
print("Fin de programa")