import json
import os
import text_functions
import time 
t = text_functions.Text


with open("player.json", "r") as f:
    player = json.load(f)

class Convert():
    def __init__(data,user,exp,levels,money,strength,defense,speed,magic,role):
        data.user = user
        data.exp = exp
        data.levels = levels
        data.money = money
        data.strength = strength
        data.defense = defense
        data.speed = speed
        data.magic = magic
        data.role = role
    def __str__(data):
        return f"{data.user},{data.exp},{data.levels},{data.money},{data.strength},{data.defense},{data.speed},{data.magic},{data.role}"

def convert(user,exp,levels,money,strength,defense,speed,magic,role):
    new_player = Convert(user,exp,levels,money,strength,defense,speed,magic,role)
    player.append(new_player.__dict__)

login = input('Are you logging in or signing up? ').upper()
if 'S' in login:
    user = input('Enter a username: ')
    gooduser = ('NotGood')
    while gooduser != ('Good'):
        for players in player:
            if user != players['user']:
                print('Username not Taken, Successfully Signed Up')
                gooduser = 'Good'
            else:
                user = input('Username Taken. Enter another Username ')

    y = input('What class do you want to be ')
    if y ==('Warrior'):
        convert(user,0,1,0,5,0,0,0,y)
    elif y ==('Tank'):
        convert(user,0,1,0,0,5,0,0,y)
    elif y ==('Mage'):
        convert(user,0,1,0,0,0,0,5,y)
elif 'L' in login:
    user = input('Enter a username: ')
    for players in player:
        if user == players['user']:
            print('Logged in')
            
t.delete_all(10)
t.slow_print('Logged in!')
time.sleep(1)
t.delete()

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player, indent=4)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")