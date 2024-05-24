import json
import os
import text_functions
import time
import classes
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
Exit Game ''')).lower().capitalize()
        time.sleep(1)
        t.delete_all(10)
        return action

a = action()

while 'E' not in a:
    if 'F' in a:
        import fighting
    elif 'S' in a:
        import shop
    elif 'G' in a:
        import gamble
    elif 'T' in a:
        import training
    a = action()

t.fast_print('Thanks for playing the game and come back later!')