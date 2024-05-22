import json
import os
import text_functions
import time
import classes
from classes import Main_functions as m
t = text_functions.Text
with open("player.json", "r") as f:
    player = json.load(f)
with open("item.json", "r") as f:
    item = json.load(f)
with open("monster.json", "r") as f:
    monster = json.load(f)
with open("moves.json", "r") as f:
    moves = json.load(f)


action = m.Action()
while 'Exit' not in action:
    if 'F' in action:
        import fighting
    elif 'S' in action:
        import shop
    elif 'G' in action:
        import gamble
    elif 'T' in action:
        import training
    action = m.Action()

if 'E' in action:
    t.fast_print('Thanks for playing the game and come back later!')