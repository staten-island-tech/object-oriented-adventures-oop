from text_functions import Text 
import actions

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


actions.Tutorial()