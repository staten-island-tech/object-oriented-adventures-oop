import json
import os
import time
from classes import user
import text_functions
with open("player.json", "r") as f:
    player = json.load(f)  
with open("item.json", "r") as f:
    Items = json.load(f)  
t = text_functions.Text

with open("player.json", mode='r') as read:
    data = json.load(read)

def Training():
    y = input(t.fast_print('Would you like to train? [Y/N]: ')).upper()
    while y == 'Y':
        t.fast_print('Training each skill takes 50 experince points and returns one point for that skill.')
        for i in data:
            if x == i['user']:
                    x = input(t.fast_print('What do you want to train?: ')).lower().capitalize()
                    if i['exp'] >= 50:
                        if 'St' in x:
                            i.update({'strength':int(i['strength'])+1})
                            i.update({'exp':int(i['exp'])-50})
                            time.sleep(.5)
                            t.fast_print('Thank you for training strength, your stat boost has been applied.')
                            time.sleep(.5)
                            y = input(t.fast_print('Would you like to train again? [Y/N]: ')).lower().capitalize()
                        elif 'D' in x:
                            i.update({'defense':int(i['defense'])+1})
                            i.update({'exp':int(i['exp'])-50})
                            time.sleep(.5)
                            t.fast_print('Thank you for training defense, your stat boost has been applied.')
                            time.sleep(.5)
                            y = input(t.fast_print('Would you like to train again? [Y/N]: ')).upper()
                        elif 'M' in x:
                            i.update({'magic':int(i['magic'])+1})
                            i.update({'exp':int(i['exp'])-50})
                            time.sleep(.5)
                            t.fast_print('Thank you for training magic, your stat boost has been applied.')
                            time.sleep(.5)
                            y = input(t.fast_print('Would you like to train again? [Y/N]: ')).upper()
                        elif 'Sp' in x:
                            i.update({'speed':int(i['speed'])+1})
                            i.update({'exp':int(i['exp'])-50})
                            time.sleep(.5)
                            t.fast_print('Thank you for training speed, your stat boost has been applied.')
                            time.sleep(.5)
                            y = input(t.fast_print('Would you like to train again? [Y/N]: ')).lower().capitalize()
                    elif i['exp'] < 50:
                        t.fast_print('You do not have enough experince points to train please come back later when you have more')
                        time.sleep(1)

Training()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")