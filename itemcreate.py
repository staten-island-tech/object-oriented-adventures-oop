import json
import os

with open("item.json", "r") as f:
    item = json.load(f)

class Items():
    def __init__(self, name, strength_boost, speed_boost, defense_boost, cost, code):
        self.name = name
        self.strength_boost = strength_boost
        self.speed_boost = speed_boost
        self.defense_boost = defense_boost
        self.cost = cost
        self.code = code
    def __str__(self):
        return f"{self.name},{self.strength_boost},{self.speed_boost},{self.defense_boost},{self.cost},{self.code}"
    
def create_item(name, strength_boost, speed_boost, defense_boost, cost, code):
    new_item = Items(name, strength_boost, speed_boost, defense_boost, cost, code)
    
    item.append(new_item.__dict__)

y = 'y'
while y == ('y'):
    name = input('Name of item: ')
    strength_boost = input('Strength stat boost: ')
    defense_boost = input('Defense stat boost: ')
    speed_boost = input('Speed boost: ')
    cost = input('Cost of item: ')
    code = input('code: ')
    create_item(name, strength_boost, speed_boost, defense_boost, cost, code)
    y = input('Creating another item?')

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(item, indent=4)
    f.write(json_string)

os.remove("item.json")
os.rename(new_file, "item.json")