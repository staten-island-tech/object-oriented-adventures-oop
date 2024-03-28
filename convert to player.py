import json

test = open("data.json", encoding="utf8")

user = json.load(test)

x = input('What is your username? ')
login = ('unsuccessful')
while login == ('unsuccessful'):
    if x in user:
        print('Logged in ')
        login = ('successful')
    else:
        input('Username does not exist. Please enter again ')
        login = ('unsuccessful')

class convert():
    def convert():
        player = {}