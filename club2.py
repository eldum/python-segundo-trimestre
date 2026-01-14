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
equipo3 = Equipo("Atletico Madrid")

print("EQUIPOS:")
print("1 - FC Barcelona")
print("2 - Real Madrid") 
print("3 - Atletico Madrid")

nombre1 = input("nombre jugador 1: ")
dorsal1 = int(input("dorsal jugador 1: "))
equipo_num1 = input("equipo (1, 2 o 3): ")

jugador1 = Jugador(dorsal1, nombre1)

if equipo_num1 == "1":
    jugador1.añadir_equipo(equipo1)
elif equipo_num1 == "2":
    jugador1.añadir_equipo(equipo2)
elif equipo_num1 == "3":
    jugador1.añadir_equipo(equipo3)
else:
    print("Equipo inválido")

nombre2 = input("nombre jugador 2: ")
dorsal2 = int(input("dorsal jugador 2: "))
equipo_num2 = input("equipo (1, 2 o 3): ")

jugador2 = Jugador(dorsal2, nombre2)

if equipo_num2 == "1":
    jugador2.añadir_equipo(equipo1)
elif equipo_num2 == "2":
    jugador2.añadir_equipo(equipo2)
elif equipo_num2 == "3":
    jugador2.añadir_equipo(equipo3)
else:
    print("Equipo inválido")

nombre3 = input("nombre jugador 3: ")
dorsal3 = int(input("dorsal jugador 3: "))
equipo_num3 = input("equipo (1, 2 o 3): ")

jugador3 = Jugador(dorsal3, nombre3)

if equipo_num3 == "1":
    jugador3.añadir_equipo(equipo1)
elif equipo_num3 == "2":
    jugador3.añadir_equipo(equipo2)
elif equipo_num3 == "3":         
    jugador3.añadir_equipo(equipo3)
else:
    print("Equipo inválido")


print("\n=== EQUIPOS Y JUGADORES ===")
for equipo in [equipo1, equipo2, equipo3]:
    if equipo.jugadores_eq:  
        print(f"\n{equipo.nombre_equipo}:")
        for jugador in equipo.jugadores_eq:
            jugador.mostrar()