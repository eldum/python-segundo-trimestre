class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}")

jugador1 = Jugador(16, "PauGasol")
jugador2 = Jugador(23, "MichaelJordan")

jugador1.mostrar()
jugador2.mostrar()