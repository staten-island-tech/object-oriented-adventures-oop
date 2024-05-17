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

for p in player:
    if user == p['user']:
        play = p

def encounter():
    power = int(play['levels'])
    monsterpower = random.randrange(power-1,power+1)
    m = monster[monsterpower]
    mname = m['monster']
    print(f'You have encountered a {mname}')
    print(m)
    return m

m = encounter()

def playermove(health):
    for i in moves:
        if int(i['level']) <= int(play['levels']):
            print(i)
    move = input('What move would you like to use? ')
    for i in moves:
        if move == i['name']:
            mhpleft = (health - int(i['power']))
            return int(mhpleft)

def monstermove(health):
    phpleft = (health - int(m['attack_strength']))
    return int(phpleft)

mhp = int(m['health_level'])
mad = int(m['attack_strength'])
php = (100+int(play['defense']))
print(mhp)
print(php)

if int(p['speed']) >= int(m['speed']):
    mhp = playermove(mhp)
while mhp > 0 and php > 0:
    php = monstermove(php)
    print(f'You have been hit with {mad} damage')
    print(f'You have {php} health left')
    if mhp > 0 and php > 0:
        mhp = playermove(mhp)
        print(f'The monster has {mhp} health left')
    else:
        print('RIP you died, ending encounter')
print('You have finished the encounter!')
play.update('exp':play)