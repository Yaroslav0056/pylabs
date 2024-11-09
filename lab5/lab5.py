class Fighter:
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damagePerAttack = damage_per_attack

    def attack(self, opponent):
        opponent.health -= self.damagePerAttack

    def is_alive(self):
        return self.health > 0


class Fight:
    def __init__(self, fighter_1, fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2

    def start_fight(self):
        attacker = self.fighter_1
        defender = self.fighter_2

        while attacker.is_alive() and defender.is_alive():
            attacker.attack(defender)
            attacker, defender = defender, attacker

        if self.fighter_1.is_alive():
            print(f"The winner is {self.fighter_1.name}")
        else:
            print(f"The winner is {self.fighter_2.name}")

def main():
    fighter_1 = Fighter('Red fighter',100, 20)
    fighter_2 = Fighter('Blue fighter',100, 15)

    fight = Fight(fighter_1, fighter_2)
    fight.start_fight()
if __name__ == '__main__':
    main()
