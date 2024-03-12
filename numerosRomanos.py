class NumerosRomanos:
    def __init__(self, numeros:int)-> None:
        self.numeros = numeros
        
        
    def convertir(self):
        ListaRomanos = ["I", "V", "X", "L", "C"]
        ListaNumeros = [1,    5,  10,  50   100]
        while self.