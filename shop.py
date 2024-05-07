import text_functions
import json
import os
from classes import user
with open("player.json", "r") as f:
    player = json.load(f)  
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
      if y == ('1'):
        i.update({'money':int(i['money'])-100})
        i.update({'strength':int(i['strength'])+1})
        t.fast_print('Congratulations! You have bought the strength consumable and consumed it for 1+ strength!')
      elif y == ('2'):
        i.update({'money':int(i['money'])-100})
        i.update({'defense':int(i['defense'])+1})
        t.fast_print('Congratulations! You have bought the defense consumable and consumed it for 1+ defense!')
      elif y == ('3'):
        i.update({'money':int(i['money'])-100})
        i.update({'speed':int(i['speed'])+1})
        t.fast_print('Congratulations! You have bought the speed consumable and consumed it for 1+ speed!')
      elif y == ('4'):
        i.update({'money':int(i['money'])-500})
        i.update({'strength':int(i['strength'])+2})
        i.update({'defense':int(i['defense'])+2})
        i.update({'speed':int(i['speed'])+1})
        t.fast_print('Congratulations! You have bought the Iron armor and put it on for 2+ strength, 2+ defense, and 1+ speed')
      elif y == ('5'):
        i.update({'money':int(i['money'])-1500})
        i.update({'strength':int(i['strength'])+5})
        i.update({'defense':int(i['defense'])+5})
        i.update({'speed':int(i['speed'])+3})
        t.fast_print('Congratulations! You have bought the diamond armor and put it on for 5+ strength, 5+ defense, and 3+ speed')

shopping()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")