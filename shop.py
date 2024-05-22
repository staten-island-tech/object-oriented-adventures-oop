import text_functions
import json
import os
from classes import user
with open("player.json", "r") as f:
    player = json.load(f)  
with open("item.json", "r") as f:
    Items = json.load(f)  
t = text_functions.Text

def shopping():
  t.Load(3)
  t.fast_print('Welcome to the game shop!')
  x = input(t.fast_print('Would you like to buy an item?: [Y/N]')).upper()
  t.delete_all(3)
  if x == 'Y':
    t.fast_print(Items)
    for i in player:
      if user == i['user']:
        y = input(t.fast_print('What item would you like to buy? (use the code provided in the shop): '))
        for j in Items:
            if y == j['code']:
              if int(i['money']) >= int(j['cost']):
                i.update({'money':int(i['money'])-int(j['cost'])})
                i.update({'strength':int(i['strength'])+int(j['strength_boost'])})
                i.update({'defense':int(i['defense'])+int(j['defense_boost'])})
                i.update({'speed':int(i['speed'])+int(j['speed_boost'])})
                t.fast_print('Congratulations on buying your item!')
              elif int(i['money']) < int(j['cost']):
                t.fast_print('you are too broke to buy this please come back later when you have more money!')
  else:
     t.fast_print('Thank you for coming to shop and please come back later?')

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")