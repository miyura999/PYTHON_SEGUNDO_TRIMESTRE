class vehiculo:
    def __init__(self , marca , modelo):
        self.marca = marca
        self.modelo = modelo

    def drive (self):
        pass

class carro(vehiculo):

    def drive(self):
        print(f"Conduciendo el {self.marca}  {self.modelo} " )

class trunk(vehiculo):
    def drive(self):
        print(f"Conduciendo el {self.marca}  {self.modelo} " )


carro = carro("tovato" , "corrolla")

trunk = trunk("ford" , "F-150")

carro.drive()

trunk.drive()

