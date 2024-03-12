from automovil import Automovil
from bicicleta import Bicicleta
from camion import Camión
from moto import Moto


def main():
    moto = Moto(2, "negra")
    automovil = Automovil(4, "rojo")
    camion = Camión(6, "blanco")
    bicicleta = Bicicleta(2, "gris")
    
    moto.info()
    automovil.info()
    camion.info()
    bicicleta.info()
    
if __name__ == "__main__":
    main()