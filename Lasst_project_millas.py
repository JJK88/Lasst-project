

millas_totales = 20000
millas_remanentes = 0
ciudad = 0

ruta1 = {'Posadas':4098,'Asuncion':3858,'Sucre':9625,'La paz':7744,}
ruta2 = {'Montevideo':4474,'Sao Pablo':6503,'Rio':1119,'Maceio':2249,}


for item,value in ruta1.items():
    millas_totales -= value
    if millas_totales <= 0:
        break
    else:
        ciudad = item
        millas_remanentes = millas_totales

print(f'Con tus millas acumuladas podes ir hasta la ciudad de {ciudad}')
print(f'Millas remanentes {millas_remanentes}')

millas_totales = 20000
millas_remanentes = 0
ciudad = 0

ruta2 = {'Montevideo':4474,'Sao Pablo':6503,'Rio':1119,'Maceio':2249,}

for item,value in ruta2.items():
    millas_totales -= value
    if millas_totales <= 0:
        break
    else:
        ciudad = item
        millas_remanentes = millas_totales

print(f'Con tus millas acumuladas podes ir hasta la ciudad de {ciudad}')
print(f'Millas remanentes {millas_remanentes}')

millas_totales = 20000
millas_remanentes = 0
ciudad = 0

ruta3 = {'Cordoba':4830,'Salta':3692,'Arica':5769,'Cusco':8189,}

for item,value in ruta3.items():
    millas_totales -= value
    if millas_totales <= 0:
        break
    else:
        ciudad = item
        millas_remanentes = millas_totales

print(f'Con tus millas acumuladas podes ir hasta la ciudad de {ciudad}')
print(f'Millas remanentes {millas_remanentes}')

millas_totales = 20000
millas_remanentes = 0
ciudad = 0

ruta4 = {'Bariloche':1732,'Calafate':7471,'Punta Arenas':8241,'Ushuaia':3374,}

for item,value in ruta4.items():
    millas_totales -= value
    if millas_totales <= 0:
        break
    else:
        ciudad = item
        millas_remanentes = millas_totales

print(f'Con tus millas acumuladas podes ir hasta la ciudad de {ciudad}')
print(f'Millas remanentes {millas_remanentes}')

#hola como estas 