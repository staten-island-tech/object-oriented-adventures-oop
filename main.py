import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

##giving the story line of the game
sprint('Hello welcome to the Matthew and Wilson game!')
sprint('Welcome to Willtopia! This is where you will start your monster slaying journey.')
sprint('You will have a choice Between mulitpule classes.')
sprint('The choises are Mage, Warrior, Tank, and Ace.')
sprint('Mages have increased magic stats and magic powers.')
sprint('Warriors have increased strenght and attack power')
sprint('Tanks have increased health and defensive stats')
sprint('Aces have increased speed and a gradual increase in every other stat')
x = input(sprint('Please chose'))


""" x = input('do you want to start a new game? [Y/N]:') ##login code to the game
if x == ('Y').upper():
    import username """