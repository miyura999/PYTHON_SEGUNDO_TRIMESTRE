#exepciones personalizadas

class Miexepcion(Exception):

    def __init__(self , mensaje , codigo):

        super().__init__(mensaje)

        self.codigo = codigo

try:
    raise Miexepcion("Ocurrio un error de personalizacion " , 404)

except Miexepcion as e : 
    print(f"codigo de error {e.codigo} , Mensaje: {e}")
