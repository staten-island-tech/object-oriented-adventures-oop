import text_functions



def Tutorial():
    t = text_functions.Text
    x = input(t.slow_print('Now that you have selected your class are you ready to start your tutorial? [Y/N]:'))
    if x == ('Y'):
        t.delete
        t.slow_print('Starting Tutorial...')
        t.delete()
        t.slow_print('...')
        t.delete()
        t.slow_print('...')
        t.delete()
    else:
        t.delete
        t.slow_print('Too bad we are starting the tutorial anyway...')
        t.delete()
        t.slow_print('...')
        t.delete()
        t.slow_print('...')
        t.delete()

def Actions():
    x = input(
'''What would you like to do? 
Fight
Shop
Save and Leave Game
'''
    )
Actions()