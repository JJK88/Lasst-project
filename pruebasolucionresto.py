
facturacion = [("1", 20584), ("2", 24984), ("3", 78463), ("4", 71745), ("5", 79137), ("6", 32562), ("7", 48836),
               ("8", 77731), ("9", 43269), ("10", 22490), ("11", 54067), ("12", 28076), ("13", 37921), ("14", 49643),
               ("15", 25786), ("16", 58654), ("17", 53835), ("18", 45252), ("19", 43754), ("20", 51972), ("21", 43856),
               ("22", 22483), ("23", 69343), ("24", 72879), ("25", 38109), ("26", 73712), ("27", 54664), ("28", 30503),
               ("29", 49072), ("30", 61027)]

""""Extraigo los findes de semana y obtengo el total de todos"""
factfin = []

factfin.append(facturacion[5::7])
factfin.append(facturacion[6::7])

sumafinde = 0

for _ in factfin:
    for n in _:
        sumafinde = sumafinde + n[1]

sumatotal = 0
for _ in facturacion:
    sumatotal = sumatotal + _[1]

sumadiassemanales = sumatotal - sumafinde

""""Obtengo los cuatro días consecutivos con mayor facturación"""

cuatro_dias_consecutivos_con_mayor_facturacion = []

for i in range(len(facturacion) - 3):
    consecutivos = facturacion[i][1] + facturacion[i + 1][1] + facturacion[i + 2][1] + \
                   facturacion[i + 3][1]
    cuatro_dias_consecutivos_con_mayor_facturacion.append(consecutivos)

maximo = max(cuatro_dias_consecutivos_con_mayor_facturacion)

for i in range(len(cuatro_dias_consecutivos_con_mayor_facturacion)):
    if cuatro_dias_consecutivos_con_mayor_facturacion[i] == maximo:
        print(facturacion[i][0], facturacion[i + 1][0], facturacion[i + 2][0],
              facturacion[i + 3][0])

print("\nPunto '1' de la Sección '1'\n")
print(f'Total facturado los días de semana $ {sumadiassemanales} pesos y los fines de semana $ {sumafinde} pesos')

"""Ordeno la facturación de menor a mayor y de mayor a menor"""
print("\nPunto '2' de la Sección '1'\n")
facturacion.sort(key=lambda x: x[1])
print(f''
      f'Los dos días con menor facturación fueron el día {facturacion[0][0]} y el día {facturacion[1][0]}')
facturacion.sort(key=lambda x: x[1], reverse=True)
print(f''
      f'Los dos días con mayor facturación fueron el día {facturacion[0][0]} y el día {facturacion[1][0]}')
