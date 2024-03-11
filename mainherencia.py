from guagua import Guagua

def main():
    intercity = Guagua(asientos = 50, ruedas = 6)
    lanzaroteBus = Guagua(asientos = 80, ruedas = 8)
    
    intercity.desplazar()
    lanzaroteBus.desplazar()
    
    intercity.informacion()
    lanzaroteBus.informacion()
    
    main()