from Character import Character
import random

class Warrior(Character):
    strength= 25
    dexterity= 20
    intelligence= 18

    mana = 75 + 75*(intelligence / 100)
    health= 200 + 200*(strength / 100)
    

    def __init__(self) -> None:
        pass

    def counter(self):
        damage = random.randrange(27-31)
        print("Воин наносит сокрушительный удар топором и наносит: " + damage + "урона")
        return damage
    
    def battle_hunger(self):
        damage = 50 + 50*(self.intelligence / 100)
        self.mana = self.mana - 30
        print("Приводит врага в бешенство, замедляя его и нанося ему урон. Наносит: " + str(damage) +" урона")
        return damage
    
    def counter_helix(self):
        damage = 80 + 80*(self.intelligence / 100)
        self.mana = self.mana - 50
        print("Герой отвечает на удары противников, нанося чистый урон всем врагам вокруг себя. Наносит: " + str(damage) +" урона")
        return damage
