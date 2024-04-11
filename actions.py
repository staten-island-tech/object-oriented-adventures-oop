from text_functions import Text 


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