import json
import os

with open("player.json", "r") as f:
    player = json.load(f)

class Play():
    def login():
        x = input('What is your username? ')
        login = ('unsuccessful')
        while login == ('unsuccessful'):
            for i in player:
                if x in i['user']:
                    print('Logged in ')
                    login = ('successful')
                else:
                    x = input('Username does not exist. Please enter again ')
                    login = ('unsuccessful')
    def actions():
        x = input('''What would you like to do?
Train
Fight
''')
        if x ==('Train'):
            Train
            
class Train():
    def training():
        