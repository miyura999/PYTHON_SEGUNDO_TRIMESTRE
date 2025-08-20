class Perro:

#Atributo de clase
    especie ='mamífero'
# El método _init_ es llamado al crear el objeto (constructor)
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
#Atributos de instancia
        self.nombre = nombre

        self.raza = raza


#metodos ladrar y caminar

    def ladra(self):

        print("Guau")

    def camina(self, pasos):

        print(f"Caminando (pasos) pasos")

#Instancia del objeto

mi_perro = Perro("Toby" , "Bulldog")

mi_perro.ladra()

mi_perro.camina (10)