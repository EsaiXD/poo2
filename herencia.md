# Ejercicio 1
'''mermaid
classDiagram
    note "Veiculos de transporte"
    Transporte <|-- Guagua

    Transporte : +int ruedas
    Transporte :
    Transporte :
    Transporte :



# Ejercicio 2 
'''mermaid
classDiagram
    note "Vehículo"
    Vehículo <|-- Automovil
    Automovil <|-- Camión
    Vehículo <|-- Bicicleta
    Bicicleta <|-- Moto

    Vehículo : +int ruedas
    Vehículo : +str color 
    Vehículo : +info()




