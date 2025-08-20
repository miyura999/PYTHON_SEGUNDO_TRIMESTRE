# exepcione multiples 

try:
    archivo = open('archivo_inesistente.txt ' , 'r')

    contenido = archivo.read()

    resultado = 10 / 0

except FileNotFoundError:
    print('Error archivo no encontrado ')

except ZeroDivisionError:
    print('Error no se puede dividir por 0')

finally:
    print('esta linea se ejecuta siempre')