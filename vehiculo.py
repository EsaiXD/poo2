class Vehículo:
    def __init__ (self, ruedas:int, color:str)-> None:
        self.ruedas = ruedas
        self.color = color 
        
     
    def info(self) -> None:
        print(self.ruedas, self.color)
        
        
if __name__ == "__main__":
    automovil = Vehículo(4, "rojo")
    bicicleta = Vehículo(2, "gris")