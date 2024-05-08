import text_functions
import json
import os
from classes import user
with open("player.json", "r") as f:
    player = json.load(f)  
with open("item.json", "r") as f:
    Items = json.load(f)  
t = text_functions.Text

for load in range(3):
    t.slow_print('Loading Shop...')
    t.delete()

t.fast_print('Welcome to the game shop!')
x = input(t.fast_print('Would you like to buy an item?: [Y/N]')).upper()
t.delete_all(3)

if x == 'Y':
      t.fast_print('''here are all of the options that are avalibale for purchase:
1)Strength consumable
  Cost-$100
  Boost-1+ strength
  Code-1
2)Defense consumable
  Cost-$100
  Boost-1+ defense
  Code-2
3)speed consumable
  Cost-$100
  Boost-1+ speed
  Code-3 
4)Iron armor
  Cost-500
  Boost-2+ strength, 2+ defense, 1+ speed
  code-4
5)Diamond armor
 Cost-1500
 Boost-5+ strength, 5+ defense, 3+speed 
 Code-5  
''')

def shopping():
  for i in player:
    if user == i['user']:
      y = input(t.fast_print('What item would you like to buy? (use the code provided in the shop): '))
      for j in Items:
          if y == j['code']:
             if i['money'] >= j['cost']:
              i.update({'money':int(i['money'])-int(j['cost'])})
              i.update({'strength':int(i['strength'])+int(j['strength_boost'])})
              i.update({'defense':int(i['defense'])+int(j['defense_boost'])})
              i.update({'speed':int(i['speed'])+int(j['speed_boost'])})
             else:
              t.fast_print('you are too broke to buy this please come back later when you have more money!')

shopping()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")