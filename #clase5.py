#clase5

class calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

operacion = calculadora(2,3)
print(operacion.multiplicacion)
