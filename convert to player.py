import json
import os

test = open("user.json", encoding="utf8")
user = json.load(test)

with open("player.json", "r") as f:
    player = json.load(f)

x = input('What is your username? ')
login = ('unsuccessful')
while login == ('unsuccessful'):
    if x in user:
        print('Logged in ')
        login = ('successful')
    else:
        x = input('Username does not exist. Please enter again ')
        login = ('unsuccessful')

class Convert():
    def __init__(data,user,points,levels):
        data.user = user
        data.points = points
        data.levels = levels
    def __str__(data):
        return f"{data.user},{data.points},{data.levels}"
def convert(user,points,levels):
    new_player = Convert(user,points,levels)
    player.append(new_player.__dict__)

convert(x,0,1)
    
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")