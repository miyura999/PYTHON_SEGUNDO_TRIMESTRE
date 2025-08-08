# Escribe un algoritmo que verifique si hay asientos disponibles en un evento y reserve 
# uno. 

asientos =["libre"] *10

def mostra_estado_asientos(asientos):
    print("Estado de los asientos")
    for i, estado in enumerate(asientos):
        print(f"Asiento {i+1} : {estado}")


def verificar_reserva_asiento(asientos, numero_asiento):
    indice = numero_asiento - 1

    if 0<= indice < len(asientos):
        if asientos[indice] =="libre":
            asientos[indice] = "ocupado"
            print(f"el asiento {numero_asiento} reservado")
            return True
        else:
            print(f"El el asiento {numero_asiento} ya esta ocupado")
    else:
        print("Numero de asiento invalido")


while(True):
    print("bienvenido a nuestro cine\n1. Reservar un asiento\n2. Mostra estado de los asientos\n3. Salir")

    opcion = int(input("dSelecione una opcion entre 1-3 : "))
    if opcion != 1 and opcion != 2 and opcion != 3 :
        print("Opcion inavalida ingrese un numero entre 1-3 ")
    elif opcion == 1:
        try:
            numero_asientos=int(input("Ingrese el numero de asiento que desea reservar entre 1-10 : "))
            verificar_reserva_asiento(asientos, numero_asientos)
        except ValueError:
             print("Por favor, ingrese un número válido.")
    elif opcion == 2 :
        mostra_estado_asientos(asientos)
    
    else:
        print("has salido del sistema")






