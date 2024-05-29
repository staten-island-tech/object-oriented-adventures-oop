import random
import text_functions
import json
import os
import time
from Login_signup import user

with open("player.json", "r") as f:
    player = json.load(f)


t = text_functions.Text
t.delete_all(3)
t.Load(3)
t.fast_print('''This is the gambling room.
You can insert a certain amount of coins to win more!
But be careful, you could lose it all anytime.
Just remember 99 percent of gamblers stop before they win big.
You can only lost 100 percent of your money, you can win 2000 percent of it back.''')
time.sleep(2)
t.delete_all(5)

y = input(t.fast_print('Would you like to Begin Gambling? [Y/N]: ')).upper()
while y == ('Y'):
    for players in player:
        if user == players['user']:
            moolah = players['money']
            t.fast_print(f'Your Balance is {moolah}')
            x = int(input(t.fast_print('How much money are you going to gamble? ')))
            if int(x) <= int(players['money']):
                number = random.randrange(1,10)
                guess = int(input(t.fast_print('What is your guess 1-10? ')))
                if number == guess:
                    players.update({'money':int(moolah)+x})
                    t.fast_print('You Win!')
                    y = input(t.fast_print('Would you like to continue Gambling? [Y/N]: ')).upper()
                else:
                    players.update({'money':int(moolah)-x})
                    t.fast_print('Wa Wa You Lose')
                    y = input(t.fast_print('Would you like to continue Gambling? [Y/N]: ')).upper()
            elif int(x) > int(players['money']):
                t.fast_print('Sorry you are too broke to gamble this amount of money please come back later when you have enough.')
                time.sleep(1)
                y = input(t.fast_print('Would you like to continue Gambling? [Y/N]: ')).upper()
if y == ('N'):
    t.fast_print('Thank you for coming to the gambling room please come back later!')
    from main import action

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")