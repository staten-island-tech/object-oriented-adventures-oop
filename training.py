import json

test = open("player.json", encoding="utf8")
user = json.load(test)

with open("player.json", "r") as f:
    player = json.load(f)


def Training(x):
    for i in player:
        if x == i:
            y = input('What do you want to train? ')
            if y == ('Strength'):
                i.update({'strength':i['strength'] + 1})
            elif y == ('Defense'):
                i.update({'defense':i['defense'] + 1})
            elif y == ('Magic'):
                i.update({'magic':i['magic'] + 1})
            elif y == ('Speed'):
                i.update({'speed':i['speed'] + 1})

Training()