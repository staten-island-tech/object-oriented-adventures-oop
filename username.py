import json
import os


with open("user.json", "r") as f:
    usernames = json.load(f)

username = input('Enter a username: ')
gooduser = ('NotGood')
while gooduser != ('Good'):
    if username not in usernames:
        print('Username not Taken')
        usernames.append(username)
        gooduser = 'Good'
    else:
        username = input('Username Taken. Enter another Username ')


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(usernames)
    f.write(json_string)

os.remove("user.json")
os.rename(new_file, "user.json")