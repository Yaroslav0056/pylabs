class Fighter:
    def __init__(self, name='', health=0, damage_per_attack=0):
        self.name = name
        self.health = health
        self.damagePerAttack = damage_per_attack

    def attack(self, opponent):
        opponent.health -= self.damagePerAttack

    def is_alive(self):
        return self.health > 0

fighters = [
    Fighter("Red Fighter", 100, 20),
    Fighter("Blue Fighter", 120, 15),
    Fighter("Yellow Fighter", 150, 25),
    Fighter("Green Fighter", 110, 18),
    Fighter("Black Fighter", 130, 22),
    Fighter("White Fighter", 90, 17),
    Fighter("Purple Fighter", 140, 24),
    Fighter("Orange Fighter", 115, 19),
    Fighter("Pink Fighter", 125, 21),
    Fighter("Silver Fighter", 105, 16),
    Fighter("Gold Fighter", 160, 30),
    Fighter("Grey Fighter", 135, 23),
    Fighter("Brown Fighter", 110, 20),
    Fighter("Cyan Fighter", 120, 18),
    Fighter("Teal Fighter", 125, 22),
    Fighter("Magenta Fighter", 140, 26)
]

