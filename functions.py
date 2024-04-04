import sys,time

class Text():
    
    def sprint(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(2./90)
    
    def delete_last():
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    

Text.sprint('Loading game ...')
delete_last()
Text.sprint('Loading game ...')
delete_last()
Text.sprint('Loading game ...')
delete_last()
Text.sprint('Loading game ...')
delete_last()
Text.sprint('Loading game ...')
delete_last()
Text.sprint('Welcome to Pythonia! This is where you will start your monster slaying journey.')
Text.sprint('You will have a choice Between mulitpule classes.')
Text.sprint('The choises are Mage, Warrior, Tank, and Ace.')
Text.sprint('Mages have increased magic stats and magic powers.')
Text.sprint('Warriors have increased strenght and attack power')
Text.sprint('Tanks have increased health and defensive stats')
Text.sprint('Aces have increased speed and a slight increase in every other stat')