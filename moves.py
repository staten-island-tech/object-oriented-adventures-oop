import json
import os

with open("player.json", "r") as f:
    moves = json.load(f)


class Moves():
    def __init__(self, name, level, power, movetype):
        self.name = name
        self.level = level
        self.power = power
        self.movetype = movetype
    def __str__(self):
        return f"{self.name},{self.level},{self.power},{self.movetype}"

def create_moves(name, level, power, movetype):
    new_move = Moves(name, level, power, movetype)
    moves.append(new_move.__dict__)

y = 'y'
while y == ('y'):
    name = input('Name of Move')
    level = input('Level of Move')
    power = input('Power of Move')
    movetype = input('Move Type')
    create_moves(name, level, power, movetype)
    y = input('Creating another move?')

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(moves)
    f.write(json_string)

os.remove("moves.json")
os.rename(new_file, "moves.json")