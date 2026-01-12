class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None

    def añadir_equipo(self, equipo):
        self.equipo = equipo
        equipo.añadir_jugador(self) 
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}: {self.equipo.nombre_equipo}")
    
class Equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq
        self.jugadores_eq = []

    def añadir_jugador(self, jugador):  
        self.jugadores_eq.append(jugador)
        
equipo1 = Equipo("FC Barcelona")
equipo2 = Equipo("Real Madrid")

jugador1 = Jugador(11, "Raphiña")
jugador2 = Jugador(7, "Vini")
jugador3 = Jugador(25, "Mijatovic")
jugador4 = Jugador(12, "Marcelo")

jugador1.añadir_equipo(equipo1)
jugador2.añadir_equipo(equipo2)
jugador3.añadir_equipo(equipo2)
jugador4.añadir_equipo(equipo2)

print(f"{equipo2.nombre_equipo}")
for jugador in equipo2.jugadores_eq:
    jugador.mostrar()