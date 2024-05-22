import json
import os
import text_functions
import time
import classes
from classes import Main_functions
t = text_functions.Text
m = Main_functions
with open("player.json", "r") as f:
    player = json.load(f)
with open("item.json", "r") as f:
    item = json.load(f)
with open("monster.json", "r") as f:
    monster = json.load(f)
with open("moves.json", "r") as f:
    moves = json.load(f)


action = input(t.fast_print('''What is your next course of action?
Fight
Gamble
Shop
Train
Exit Game ''')).upper()
time.sleep(1)
t.delete_all(10)


if 'F' or 'S' or 'G' or 'T' in Main_functions.Action():
    if 'F' in m.Action():
        import fight

    elif 'S' in m.Action():
        from shop import shopping 
        shopping()
        m.Action()

    elif 'G' in m.Action():
        from gamble import Gamble
        Gamble()
        m.Action()

    elif 'T' in Action():
        from training import Training
        Training()
        m.Action()

else:
    t.fast_print('Thanks for playing the game and come back later!')