# Crea un algoritmo que tome una lista de nombres y fechas de cumpleaños y los organice
# por mes.

nombres_cumpleaños = {
    "Juan": "15/01/1990",
    "Ana": "22/02/1985",
    "Luis": "10/03/1992",
    "María": "05/04/1988",
    "Pedro": "18/05/1995",
    "Laura": "30/06/1991",
    "Carlos": "12/07/1987",
}

def lista_oganizada(nombres_cumpleaños):
    meses = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
    
    for nombre, fecha in nombres_cumpleaños.items():
        mes = int(fecha.split("/")[1])
        meses[mes].append(nombre)
    
    return meses

meses_cumpleaños = lista_oganizada(nombres_cumpleaños)

for mes, nombres in meses_cumpleaños.items():

    print(f"mes {mes} , {nombres} tienen cumpleaños en este mes.")
    