import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("-------Plantilla por turnos-------")

sqlturnos = """
    select distinct TURNO, case TURNO 
    when 'T' then 'TARDE' 
    when 'M' then 'MAÑANA' 
    else 'NOCHE' 
    end as VALOR
    from PLANTILLA
"""
cursor = connection.cursor()
cursor.execute(sqlturnos)
listaTurnos = []
contador = 1
for row in cursor:
    listaTurnos.append(row[0])
    print(f"{contador} .- {row[1]}")
    contador += 1
cursor.close()
print("Seleccione una opción")
opcion = int(input()) - 1
turno = listaTurnos[opcion]
sqlplantilla = "select * from PLANTILLA where TURNO=:p1"
cursor = connection.cursor()
cursor.execute(sqlplantilla, (turno,))
for row in cursor:
    print(row)
cursor.close()
connection.close()
print("Fin de programa")
