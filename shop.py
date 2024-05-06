import text_functions
import json
import os
with open("player.json", "r") as f:
    player = json.load(f)  
t = text_functions.Text

for load in range(3):
    t.slow_print('Loading Shop...')
    t.delete()

t.fast_print('Welcome to the game shop!')
x = input(t.fast_print('Would you like to buy an item?: [Y/N]'))
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

def Shop(user):
     for player in player:
          if user == player['user']:
               money = player["money"]
               t.fast_print(f'Your balance is: {money}')