import json
import os

with open("monster.json", "r") as f:
    monster = json.load(f)

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
    
    monster.append(new_Monster.__dict__)

y = 'y'
while y == ('y'):
    name = input('Name of monster: ').capitalize()
    monster_level = input('Level of monster: ')
    attack_strength = input('attack strength of monster: ')
    health_level = input('monster health: ')
    speed = input('speed: ')
    experince_dropped = input('experince dropped: ')
    money_dropped = input('money dropped: ')

    create_monster(name, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped)
    y = input('Creating another move?').lower()


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(monster, indent=4)
    f.write(json_string)

os.remove("monster.json")
os.rename(new_file, "monster.json")