class Jugador:
    def __init__(self, dorsal, nombre, equipo):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = equipo
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}: {self.equipo.nombre_equipo}")
    
class Equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq

equipo1 = Equipo("Lakers")
equipo2 = Equipo("Ducati")

jugador1 = Jugador(16, "PauGasol", equipo1)
jugador2 = Jugador(47, "Marc Marquez", equipo2)

jugador1.mostrar()
jugador2.mostrar()