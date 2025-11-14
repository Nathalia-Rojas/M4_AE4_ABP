from persona import Persona
from tamagotchi import Tamagotchi

if __name__ == "__main__":
    mi_tamagotchi = Tamagotchi("Luna", "Rosa")
    persona = Persona("Nathalia", "Rojas", mi_tamagotchi)

    persona.darle_comida()
    persona.jugar_con_tamagotchi()
    persona.curarlo()

