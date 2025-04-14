class Calculadora:
    def __init__(self):
        pass

    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y
    
    def divisao(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y