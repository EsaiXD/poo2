class Transporte:
    def __init__(self, *, ruedas:int, asientos:int) -> None:
        self.ruedas = ruedas 
        self.asientos = asientos
    
        pass
    
    def desplazar(x:int, y:int = 0) -> None:
        print("Desplazamiento a:", x, y)
        
    def informacion(self) -> None:
        print()