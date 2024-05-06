import text_functions
import json
import os
from classes import user

with open("player.json", "r") as f:
    player = json.load(f)

with open("monster.json", "r") as f:
    monster = json.load(f)

text_functions.Load(3)
t = text_functions.Text
t.fast_print('''This is the fighting system.
You can fight monsters to level up and gain money.
These Monsters are strong, 
I suggest training to be able to beat them.''')
t.delete_all(4)

cont = input('Do you wish to continue? Yes/No')
if cont == ('Yes'):
    print('Starting Encounter')

def encounter(user):
    for players in player:
        if user == players['user']:
            