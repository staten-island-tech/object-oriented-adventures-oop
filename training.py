import json
import os
from classes import user

with open("player.json", mode='r') as read:
    data = json.load(read)

def Training(x):
    for i in data:
        if x == i['user']:
            y = input('What do you want to train? ')
            if y == ('Strength'):
                i.update({'strength':int(i['strength'])+1})
            elif y == ('Defense'):
                i.update({'defense':int(i['defense'])+1})
            elif y == ('Magic'):
                i.update({'magic':int(i['magic'])+1})
            elif y == ('Speed'):
                i.update({'speed':int(i['speed'])+1})

Training(user)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")