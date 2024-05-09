import text_functions
import json
import os
from classes import user
import random

with open("player.json", "r") as f:
    player = json.load(f)

with open("monster.json", "r") as f:
    monster = json.load(f)

with open("moves.json", "r") as f:
    moves = json.load(f)


text_functions.Load(3)
t = text_functions.Text
t.fast_print('''This is the fighting system.
You can fight monsters to level up and gain money.
These Monsters are strong, 
I suggest training to be able to beat them.''')
t.delete_all(4)

cont = input('Do you wish to continue? Yes/No ')
if cont == ('Yes'):
    print('Starting Encounter')

class Fight():
    def __init__(self):
        for players in player:
            if user == players['user']:
                power = int(players['levels'])
                monsterpower = random.randrange(power-1,power+1)
                for monsters in monster:
                    if monsterpower == int(monsters['monster_level']):
                        self.m = monsters['monster']
                        print(f'You have encountered a {self.m}')
                        print(monsters)
    def squareup():
        for players in player:
            if user == players['user']:
                for mo in moves:
                    if int(mo['level']) <= int(players['levels']):
                        print(mo)
        


Fight()