class familiaProgramadores : 
    
    def __init__(self , nombre : str , apellido : str ):
        self.nombre = nombre
        self.apellido = apellido 

    def saludar(self):
        print(f"hola soy ${self.nombre } y soy un programador ")

    def trabajar(self) : 
        print("estor tarabajando en proyecto emocionante ")


class hijoProgramador(familiaProgramadores):

    def __init__(self, nombre: str , lenguaje: str , apellido: str):
        super().__init__(nombre , apellido)
        self.lenguaje = lenguaje 

    def programar(self):
        print(f"estoy programando enn ${self.lenguaje}")

hijo = hijoProgramador("juan" , "python" , "gomez")

hijo.saludar()
hijo.programar()

