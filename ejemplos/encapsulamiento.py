class persona:

    def __init__(self, nombre:str , edad:int , direccion:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__direcccion = direccion

    def setDireccion(self , direccion ):
        self.__direcccion = direccion

    def getDireccion(self):
        return self.__direcccion
    

p = persona("Juan",  25 , "Av siempre viva 123")
p.setDireccion("Calle falsa 123")

print(p.getDireccion())

