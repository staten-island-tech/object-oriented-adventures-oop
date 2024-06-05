import json
import os
import text_functions
import time
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
    action = input(t.fast_print('''What is your next course of action?
Fight
Gamble
Shop
Train
Exit Game''')).lower().capitalize()
    time.sleep(1)
    t.delete_all(10)
    while 'E' not in action:
        if 'F' in action:
            import fighting
        elif 'S' in action:
            import shop
        elif 'G' in action:
            import gamble
        elif 'T' in action:
            import training
        else:
            print('You have not entered a valid option')
    t.fast_print('Thanks for playing the game and come back later!')

action()
