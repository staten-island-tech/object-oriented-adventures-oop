import json
import os

with open("monster.json", "r") as f:
    moves = json.load(f)

class Monster():
    def __init__(data,name, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped ):
        data.monster = name 
        data.monster_level = monster_level
        data.attack_strength = attack_strength
        data.health_level = health_level
        data.speed = speed
        data.experince_dropped = experince_dropped
        data.money_dropped = money_dropped

    def __str__(data):
        return f"{data.name},{data.monster_level},{data.attack_strength},{data.health_level},{data.speed},{data.experince_dropped},{data.money_dropped}"

def create_monster(name, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped):
    new_Monster = Monster(name, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped)
    
    moves.append(new_Monster.__dict__)

y = 'y'
while y == ('y'):
    name = input('Name of Move: ')
    monster_level = input('Level of Move: ')
    attack_strength = input('Power of Move: ')
    health_level = input('Move Type: ')
    speed = input('speed: ')
    experince_dropped = input('experince dropped: ')
    money_dropped = input('money dropped: ')

    create_monster(name, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped)
    y = input('Creating another move?')

create_monster()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(moves)
    f.write(json_string)

os.remove("moves.json")
os.rename(new_file, "moves.json")