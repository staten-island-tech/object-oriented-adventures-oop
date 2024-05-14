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
    def encounter():
        for players in player:
            if user == players['user']:
                power = int(players['levels'])
                monsterpower = random.randrange(power-1,power+1)
                m = monster[monsterpower]
                mname = m['monster']
                print(f'You have encountered a {mname}')
                return m
    def playermove():
        m = Fight.encounter()
        print(m)
        for players in player:
            if user == players['user']:
                for i in moves:
                    if int(i['level']) <= int(players['levels']):
                        print(i)
                move = input('What move would you like to use? ')
                for i in moves:
                    if move == i['name']:
                        hpleft = (int(m['health_level']) - int(i['power']))
                        print(hpleft)
            
        

Fight.playermove()