
from Character import Character
# import math
import random

class Mage(Character):
    name = "Mage"

    strength= 20
    dexterity= 23
    intelligence= 30

    mana = 75 + 75*(intelligence / 100)
    health= 200 + 200*(strength / 100)
    

    def __init__(self) -> None:
        pass

    def simple__attack(self, character):
        damage = random.randrange(19-31)
        # character.health = character.health - damage
        print("Маг наносит сокрушительный удар огненным шаром и наносит: " + damage + "урона")
        return damage
    
    def dargon_slave(self):
        damage = 85 + 85*(self.intelligence / 100)
        self.mana = self.mana - 60
        print("Герой высвобождает дыхание дракона, сжигающее всех на своём пути. Наносит: " + str(damage) +" урона")
        return damage
    
    def light_strike_array(self):
        damage = 80 + 80*(self.intelligence / 100)
        self.mana = self.mana - 50
        print("Призывает столб пламени, который оглушает врагов и наносит им урон. Наносит: " + str(damage) +" урона")
        return damage

    

