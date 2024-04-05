import json

test = open("player.json", encoding="utf8")
user = json.load(test)

with open("player.json", "r") as f:
    player = json.load(f)


def Training(x):
    for i in player:
        if x == i['user']:
            y = input('What do you want to train? ')
            if y == ('Strength'):
                i['strength'] += 1
            elif y == ('Defense'):
                i['defense'] += 1
            elif y == ('Magic'):
                i['magic'] += 1
            elif y == ('Speed'):
                i['speed'] += 1

Training('hi')