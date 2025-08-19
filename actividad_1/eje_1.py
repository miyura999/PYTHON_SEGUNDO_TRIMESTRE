# ü .Crea una clase Racional que permita trabajar con números racionales (fracciones). Incluye los siguientes métodos: constructores (por defecto y parametrizado), accedentes, leer(), suma, resta, multiplicación, división.

class racional:
    def __init__(self , numerador1 , denominador1 , numerador2 , denominador2):
        self.numerador1 = numerador1
        self.denomindor1 = denominador1
        self.numerador2 = numerador2
        self.denomindor2 = denominador2

class operaciones(racional):

    def suma1(self):
        suma1=((self.numerador1*self.denomindor2)+(self.denomindor1*self.numerador2))
        return suma1
    
    def suma2(self):
        suma2=self.denomindor1*self.denomindor2
        return suma2
    
    def resta1(self):
        resta1=((self.numerador1*self.denomindor2)-(self.denomindor1*self.numerador2))
        return resta1
    
    def resta2(self):
        resta2=self.denomindor1*self.denomindor2
        return resta2

    def multi1(self):
        multi1=(self.numerador1*self.numerador2)
        return multi1

    def multi2(self):
        multi2=(self.denomindor1*self.denomindor2)
        return multi2
    
    def divi1(self):
        divi1=(self.numerador1*self.denomindor2)
        return divi1
    
    def divi2(self):
        divi2=(self.denomindor1*self.numerador2)
        return divi2




operaciones=operaciones(3 , 4 , 5 , 7)
print("El resultado de la suma es: " , operaciones.suma1() , "/" , operaciones.suma2())

print("El resultado de la resta es: " , operaciones.resta1() , "/" , operaciones.resta2())

print("El resultado de la multiplicacion es: " , operaciones.multi1() , "/" , operaciones.multi2())

print("El resultado de la division es: " , operaciones.divi1() , "/" , operaciones.divi2())




