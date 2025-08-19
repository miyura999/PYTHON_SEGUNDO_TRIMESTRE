# ü Crea una clase Cuenta (bancaria) con atributos para el número de cuenta (un entero largo), el DNI del cliente (otro entero largo), el saldo actual y el interés anual que se aplica a la cuenta (porcentaje). Define en la clase los siguientes métodos:

# — Constructor por defecto y constructor con DNI, saldo e interés

# - Accedentes y mutadores. Para el número de cuenta no habrá mutador.

# - actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365 aplicado al saldo actual).

# - ingresar(double): permitirá ingresar una cantidad en la cuenta.

# - retirar(double): permitirá sacar una cantidad de la cuenta (si hay saldo). –

# - Método que nos permita mostrar todos los datos de la cuenta.

class cuenta:

    def __init__(self , numeroCuenta , dniCliente , saldo: 0 , interesAnual: 0):

        self.__numeroCuenta = numeroCuenta
        self.__dniCliente = dniCliente
        self.__saldo_actual = saldo 
        self.__interesAnual = interesAnual

    def numeroCuenta(self):
        return self.__numeroCuenta
    
    def dniCliente(self):
        return self.__dniCliente
    
    def saldo_actual(self):
        return self.__saldo_actual

    def saldo_actual(self, nuevo_saldo):
        self.__saldo_actual = nuevo_saldo
    
    def interes_anual(self):
        return self.__intresAnual

    def interes_anual(self, nuevo_interes):
        self.__interesAnual = nuevo_interes

    def actualizarSaldo(self):
        interesDiario=self.__interesAnual/365
        self.__saldo_actual =(self.__saldo_actual + self.__saldo_actual)*interesDiario

        print("saldo actualizado con el interez diario")

    def ingresar(self , cantidad):
        if cantidad > 0:
            self.__saldo_actual = self.__saldo_actual + cantidad
            print(f"se agrego {cantidad} su saldo actual es {self.__saldo_actual}")
        
        else:
            print("no se pueden ingresar numeros negativos")

    def retirar(self , retirar):
        if retirar > self.__saldo_actual :
            print("la cantidad a retirar en mayor al saldo")

        else:
            self.__saldo_actual = self.__saldo_actual - retirar
            print(f"se retiraron {retirar} su saldo actual es {self.__saldo_actual}")

    def mostrar_datos(self):
        print("\n--- Datos de la Cuenta ---")
        print(f"Número de cuenta: {self.__numeroCuenta}")
        print(f"DNI del cliente: {self.__dniCliente}")
        print(f"Saldo actual: ${self.__saldo_actual:.2f}")
        print(f"Interés anual: {self.__interesAnual:.2f}%")
        print("--------------------------\n")

# Ejemplo de uso
cuenta1 = cuenta(123456789, 987654321, 1000.0, 5.0)
cuenta1.mostrar_datos()         
cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)
cuenta1.actualizarSaldo()
cuenta1.mostrar_datos()  # Mostrar datos actualizados












