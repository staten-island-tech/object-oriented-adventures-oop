import json
import os

test = open("player.json", encoding="utf8")
player = json.load(test)




def Training(x):
    for i in player:
        if x == i['user']:
            y = input('What do you want to train? ')
            if y == ('Strength'):
                i.update({'strength':int(i['strength'])+1})
            elif y == ('Defense'):
                i['defense'] += 1
            elif y == ('Magic'):
                i['magic'] += 1
            elif y == ('Speed'):
                i['speed'] += 1

Training('hi')

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")