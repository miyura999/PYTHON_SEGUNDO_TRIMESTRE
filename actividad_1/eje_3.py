# ü Crea las siguientes clases :

# - Motor: con métodos para arrancar el motor y apagarlo.

# - Rueda: con métodos para inflar la rueda y desinflarla. Ventana: con métodos para abrirla y cerrarla.

# - Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta.

# - Coche: con un motor, cuatro ruedas y dos puertas; con los métodos que te parezcan adecuados

class vehiculo:

    def __init__(self , nombre):
        self.nombre = nombre

    def drive(self):
        pass


class motor(vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def arrancar(self):
        print(f"El motor del {self.nombre} está arrancado.")

    def apagar(self):
        print(f"El motor del {self.nombre} está apagado.")

class rueda(vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def inflar(self):
        print(f"La rueda del {self.nombre} está inflada.")

    def desinflar(self):
        print(f"La rueda del {self.nombre} está desinflada.")

class ventana(vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def abrir(self):
        print(f"La ventana del {self.nombre} está abierta.")

    def cerrar(self):
        print(f"La ventana del {self.nombre} está cerrada.")

class puerta(vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ventana = ventana(nombre)

    def abrir(self):
        print(f"La puerta del {self.nombre} está abierta.")
        self.ventana.abrir()

    def cerrar(self):
        print(f"La puerta del {self.nombre} está cerrada.")
        self.ventana.cerrar()

class coche(vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.motor = motor(nombre)
        self.ruedas = [rueda(nombre) for _ in range(4)]
        self.puertas = [puerta(nombre) for _ in range(2)]

    def arrancar(self):
        self.motor.arrancar()
        for rueda in self.ruedas:
            rueda.inflar()

    def apagar(self):
        self.motor.apagar()
        for rueda in self.ruedas:
            rueda.desinflar()

    def abrir_puertas(self):
        for puerta in self.puertas:
            puerta.abrir()

    def cerrar_puertas(self):
        for puerta in self.puertas:
            puerta.cerrar()

# Ejemplo de uso
mi_coche = coche("Toyota Corolla")  
mi_coche.arrancar()
mi_coche.abrir_puertas()
mi_coche.cerrar_puertas()
mi_coche.apagar()


