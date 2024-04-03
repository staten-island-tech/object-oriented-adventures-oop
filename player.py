import json
import os

test = open("user.json", encoding="utf8")
user = json.load(test)

with open("player.json", "r") as f:
    player = json.load(f)

username = input('Enter a username: ')
gooduser = ('NotGood')
while gooduser != ('Good'):
    for usernames in player:
        if username != usernames['user']:
            print('Username not Taken')
            usernames.append(username)
            gooduser = 'Good'
        else:
            username = input('Username Taken. Enter another Username ')

class Convert():
    def __init__(data,user,exp,levels,strength,defense,speed,magic,role):
        data.user = user
        data.exp = exp
        data.levels = levels
        data.strength = strength
        data.defense = defense
        data.speed = speed
        data.magic = magic
        data.role = role
    def __str__(data):
        return f"{data.user},{data.levels},{data.exp},{data.strength},{data.defense},{data.speed},{data.magic},{data.role}"
def convert(user,exp,levels,strength,defense,speed,magic,role):
    new_player = Convert(user,exp,levels,strength,defense,speed,magic,role)
    player.append(new_player.__dict__)

y = input('What class do you want to be')
if y ==('Warrior'):
    convert(username,0,1,5,0,0,0,y)
elif y ==('Tank'):
    convert(username,0,1,0,5,0,0,y)
elif y ==('Mage'):
    convert(username,0,1,0,0,0,5,y)
elif y ==('Ace'):
    convert(username,0,1,0,0,5,0,y)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")