import text_functions
t = text_functions.Text

for load in range(3):
    t.slow_print('Loading Shop...')
    t.delete()

t.fast_print('Welcome to the game shop!')
x = input(t.fast_print('Would you like to buy an item?: [Y/N]'))
t.delete_all(3)

if x == 'Y':
      t.fast_print('''here are all of the options that are avalibale for purchase:
1)Strength consumable
  Cost-$100
  Boost-1+ strength
  Code-SC1
2)Defense consumable
  Cost-$100
  Boost-1+ defense
  Code-DC1

3)
                   
                   
                   
                   
                   
                   
                   
                   
                   ''')