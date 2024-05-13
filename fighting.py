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

def encounter():
    for players in player:
        if user == players['user']:
            power = int(players['levels'])
            monsterpower = random.randrange(power-1,power+1)
            m = monster[monsterpower]
            mname = m['monster']
            print(f'You have encountered a {mname}')
            print(m)
            return m
def squareup():
    m = encounter()
    for players in player:
        if user == players['user']:
            [print(moves[i]) for i in range(0,int(players['levels']))]
            move = input('What move would you like to use? ')
            
        

squareup()