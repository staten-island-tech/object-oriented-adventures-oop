usernames = []
username = input('Enter a username: ')
gooduser = ('NotGood')
while gooduser != ('Good'):
    for i in usernames:
        if username == i:
            username = input('Username Taken. Enter another username ')
            gooduser = ('NotGood')
        else:
            usernames.append(username)
            gooduser = ('Good')
print(usernames)