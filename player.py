usernames = ['hi','bye'] 
"""username = input('Enter a username: ')
gooduser = ('NotGood')
while gooduser != ('Good'):
    if [(username != i) for i in usernames]:
        print('Username not Taken')
        usernames.append(username)
        gooduser = 'Good'
    else:
        username = input('Username Taken. Enter another Username ')
print(usernames)
 """
print([i for i in usernames])