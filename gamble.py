import random
import text_functions
import json
import os
import time
from classes import user

with open("player.json", "r") as f:
    player = json.load(f)


t = text_functions.Text
t.delete_all(3)
text_functions.Load(3)
t.fast_print('''This is the gambling room.
You can insert a certain amount of coins to win more!
But be careful, you could lose it all anytime.
Just remember 99 percent of gamblers stop before they win big.
You can only lost 100 percent of your money, you can win 2000 percent of it back.''')
time.sleep(3)
t.delete_all(5)

def Gamble(user):
    for players in player:
        if user == players['user']:
            moolah = players['money']
            print(f'Your Balance is {moolah}')
            x = int(input('How much money are you going to gamble? '))
            number = random.randrange(1,10)
            guess = int(input('What is your guess 1-10? '))
            if number == guess:
                players.update({'money':int(moolah)+x})
                print('You Win!')
            else:
                players.update({'money':int(moolah)-x})
                print('Wa Wa You Lose')


Gamble(user)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")