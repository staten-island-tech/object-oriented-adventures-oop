import random
import text_functions
import json
import os
from classes import user

with open("player.json", "r") as f:
    player = json.load(f)


t = text_functions.Text
for load in range(3):
    t.slow_print('Loading game ...')
    t.delete()
t.fast_print('''This is the gambling room.
You can insert a certain amount of coins to win more!
But be careful, you could lose it all anytime.
Just remember 99 percent of gamblers stop before they win big.
You can only lost 100 percent of your money, you can win 2000 percent of it back.''')
t.delete_all(5)

def Gamble(user):
    for players in player:
        if user == players['user']
        print(f'Your Balance is {players['money']}')
    x = input('How much money are you going to gamble?')
