import text_functions

t = text_functions.Text
t.slow_print('Loading game ...')
t.delete()
t.slow_print('Loading game ...')
t.delete()
t.slow_print('Loading game ...')
t.delete()
t.slow_print('Loading game ...')
t.delete()
t.slow_print('Loading game ...')
t.delete()
t.fast_print('Welcome to Pythonia! This is where you will start your monster slaying journey.')
t.fast_print('You will have a choice Between mulitpule classes.')
t.fast_print('The choises are Mage, Warrior, Tank, and Ace.')
t.fast_print('Mages have increased magic stats and magic powers.')
t.fast_print('Warriors have increased strength and attack power')
t.fast_print('Tanks have increased health and defensive stats')
t.fast_print('Please select your class next')
t.delete_all(8)
import classes

action = input('''What is your next course of action?
Fight
Train
Shop
''')
if action == 'Fight':
    import fight
elif action == 'Train':
    import training
elif action == 'Shop':
    import shop
elif action == 'Gamble':
    import gamble
