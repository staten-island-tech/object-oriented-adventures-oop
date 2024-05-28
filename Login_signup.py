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
t.delete()
if 'S' in login: 
    t.Load(1)
    t.fast_print('Welcome to Pythonia! This is where you will start your monster slaying journey.')
    t.fast_print('You will have a choice Between mulitpule classes.')
    t.fast_print('The choises are Mage, Warrior, Tank, and Ace.')
    t.fast_print('Mages have increased magic stats and magic powers.')
    t.fast_print('Warriors have increased strength and attack power')
    t.fast_print('Tanks have increased health and defensive stats')
    input(t.fast_print('Click enter when you are ready to select your username and class'))
    t.delete_all(10)
    user = input('Enter a username: ')
    gooduser = ('NotGood')
    while gooduser != ('Good'):
        for players in player:
            if user != players['user']:
                print('Username not Taken, Successfully Signed Up')
                gooduser = 'Good'
                break
            else:
                user = input('Username Taken. Enter another Username ')

    y = input('What class do you want to be ')
    if y ==('Warrior'):
        convert(user,0,1,0,5,0,0,0,y)
    elif y ==('Tank'):
        convert(user,0,1,0,0,5,0,0,y)
    elif y ==('Mage'):
        convert(user,0,1,0,0,0,0,5,y)
    t.fast_print('Congrats on joining the game!')
    time.sleep(1)
    t.delete_all(30)

    
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