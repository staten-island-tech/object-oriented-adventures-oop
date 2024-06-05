import json
import os
import text_functions
import time
from Login_signup import user

t = text_functions.Text
with open("player.json", "r") as f:
    player = json.load(f)
with open("item.json", "r") as f:
    item = json.load(f)
with open("monster.json", "r") as f:
    monster = json.load(f)
with open("moves.json", "r") as f:
    moves = json.load(f)

def action():
    game = 'z'
    while game != 'Done':    
        action = input(t.fast_print('''What is your next course of action?
Fight - 1
Gamble - 2
Shop - 3
Train - 4
Exit Game - 5''')).lower().capitalize()
        time.sleep(1)
        t.delete_all(10)
        if '1' in action:
            import fighting
        elif '2' in action:
            import shop
        elif '3' in action:
            import gamble
        elif '4' in action:
            import training
        elif '5' in action:
            game = 'Done'
        else:
            print('You have not entered a valid option')
    t.fast_print('Thanks for playing the game and come back later!')

action()
