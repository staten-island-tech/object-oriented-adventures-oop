from text_functions import Text 

Text.slow_print('Loading game ...')
Text.delete()
Text.slow_print('Loading game ...')
Text.delete()
Text.slow_print('Loading game ...')
Text.delete()
Text.slow_print('Loading game ...')
Text.delete()
Text.slow_print('Loading game ...')
Text.delete()
Text.fast_print('Welcome to Pythonia! This is where you will start your monster slaying journey.')
Text.fast_print('You will have a choice Between mulitpule classes.')
Text.fast_print('The choises are Mage, Warrior, Tank, and Ace.')
Text.fast_print('Mages have increased magic stats and magic powers.')
Text.fast_print('Warriors have increased strenght and attack power')
Text.fast_print('Tanks have increased health and defensive stats')
Text.fast_print('Aces have increased speed and a slight increase in every other stat')
Text.fast_print('Please select your class next')
Text.delete_all(8)

def Tutorial():
    x = input(Text.slow_print('Now that you have selected your class are you ready to start your tutorial? [Y/N]:'))
    if x == ('Y'):
        Text.delete
        Text.slow_print('Starting Tutorial...')
        Text.delete()
        Text.slow_print('...')
        Text.delete()
        Text.slow_print('...')
        Text.delete()
    else:
        Text.delete
        Text.slow_print('Too bad we are starting the tutorial anyway...')
        Text.delete()
        Text.slow_print('...')
        Text.delete()
        Text.slow_print('...')
        Text.delete()

Tutorial()