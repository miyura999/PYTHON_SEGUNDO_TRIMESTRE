class fichero:

    def __init__(self , nombre_fichero):
        print("iniciando fichero")
        self.nombre_fichero = nombre_fichero



    def __enter__(self):
        print("entrando al fichero")
        self.fichero = open(self.nombre_fichero , "w")
        return self.fichero

    def __exit__(self , exc_type , exc_val , exc_tb):
        if self.fichero:
            print("saliendo del fichero ")
            self.fichero.close()
            
with fichero('fichero.txt') as fichero:
    print("usando el contex manager")
    fichero.write("hola mundo")