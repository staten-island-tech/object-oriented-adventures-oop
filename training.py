import json
import os
import time
from Login_signup import user
import text_functions
with open("player.json", "r") as f:
    player = json.load(f)  
with open("item.json", "r") as f:
    Items = json.load(f)  
t = text_functions.Text

with open("player.json", mode='r') as read:
    data = json.load(read)

x = user

y = input(t.fast_print('Would you like to train? [Y/N]: ')).upper()
t.delete_all(2)
while y == 'Y':
    t.fast_print('Training each skill takes 50 experince points and returns one point for that skill.')
    t.fast_print('You can train Strength, Defense, Speed, and Magic.')
    input(t.fast_print('Click enter when you are ready to continue.'))
    t.delete_all(10)
    for i in data:
        if x == i['user']:
                z = input(t.fast_print('What do you want to train?: ')).lower().capitalize()
                t.delete_all(2)
                if i['exp'] >= 5:
                    if 'St' in z:
                        i.update({'strength':int(i['strength'])+1})
                        i.update({'exp':int(i['exp'])-5})
                        time.sleep(.5)
                        t.fast_print('Thank you for training strength, your stat boost has been applied.')
                        time.sleep(1)
                        t.delete_all(3)
                        y = input(t.fast_print('Would you like to train again? [Y/N]: ')).lower().capitalize()
                        t.delete()
                    elif 'D' in z:
                        i.update({'defense':int(i['defense'])+1})
                        i.update({'exp':int(i['exp'])-5})
                        time.sleep(.5)
                        t.fast_print('Thank you for training defense, your stat boost has been applied.')
                        time.sleep(1)
                        t.delete_all(3)
                        y = input(t.fast_print('Would you like to train again? [Y/N]: ')).upper()
                        t.delete()
                    elif 'M' in z:
                        i.update({'magic':int(i['magic'])+1})
                        i.update({'exp':int(i['exp'])-5})
                        time.sleep(.5)
                        t.fast_print('Thank you for training magic, your stat boost has been applied.')
                        time.sleep(1)
                        t.delete_all(3)
                        y = input(t.fast_print('Would you like to train again? [Y/N]: ')).upper()
                        t.delete()
                    elif 'Sp' in z:
                        i.update({'speed':int(i['speed'])+1})
                        i.update({'exp':int(i['exp'])-5})
                        time.sleep(.5)
                        t.fast_print('Thank you for training speed, your stat boost has been applied.')
                        time.sleep(1)
                        t.delete_all(3)
                        y = input(t.fast_print('Would you like to train again? [Y/N]: ')).lower().capitalize()
                        t.delete()
                elif i['exp'] < 5:
                    t.fast_print('You do not have enough experince points to train please come back later when you have more')
                    time.sleep(1)
                    t.delete_all(3)
                    y = 'N'
if y != ('Y'):
    t.fast_print('Thanks for coming please come back later!')
    time.sleep(1)
    from app import action

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")