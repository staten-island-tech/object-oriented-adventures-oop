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

action = input(t.fast_print('''What is your next course of action?
Fight
Gamble
Shop
''')).upper()

if 'F' in action:
    import fight
elif 'S' in action:
    from shop import shopping 
    shopping()
elif 'G' in action:
    from gamble import Gamble
    Gamble()
