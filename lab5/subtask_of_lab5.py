from random import shuffle
from fighters import *

class Fight:
    def __init__(self, fighter_1, fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2

    def start_fight(self):
        attacker = self.fighter_1
        defender = self.fighter_2
        print(f'{attacker.name} vs {defender.name}')

        while attacker.is_alive() and defender.is_alive():
            attacker.attack(defender)

            if not defender.is_alive():
                print(f"\033[1;31m{defender.name} has died!\033[0m")
                break

            attacker, defender = defender, attacker

        return self.fighter_1 if attacker.is_alive() else self.fighter_2

class Tournament:
    def __init__(self, fighters):
        self.fighters = fighters

    def start_tournament(self):
        if len(self.fighters) & (len(self.fighters) - 1) != 0:
            print('The number of fighters is not suitable for the tournament')
            return
        else:
            print('The tournament is starting!!!')
            self.run_tournament()

    def run_tournament(self):
        current_fighters = self.fighters[:]

        fight_number = 1
        round_number = 1
        while len(current_fighters) > 1:
            if len(self.fighters) & (len(self.fighters) - 1) != 0:
                print('The number of fighters is not suitable for the tournament')
                return
            print(f"\033[1m----------Round {round_number}----------\033[0m")
            shuffle(current_fighters)
            fighter_next_round = []

            for i in range(0, len(current_fighters), 2):
                fighter_1 = current_fighters[i]
                fighter_2 = current_fighters[i + 1]
                fight = Fight(fighter_1, fighter_2)
                winner = fight.start_fight()
                fighter_next_round.append(winner)

                print(f'Fight {fight_number}')
                print(f'{fighter_1.name} vs {fighter_2.name} ----- Winner: {winner.name}')
                print(f"Health: {fighter_1.name}: {fighter_1.health}, {fighter_2.name}: {fighter_2.health}")
                fight_number += 1

            current_fighters = fighter_next_round
            round_number += 1

        print(f"\033[1;32mThe tournament winner is {current_fighters[0].name}\033[0m!")

tournament = Tournament(fighters)
tournament.start_tournament()
