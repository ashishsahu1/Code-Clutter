import random

a = random.randint(1,9)
x = int(input('Gues the number : '))

if x==a:
    print('Damn, you guessed it right')
elif x<a:
    print('Aaaahaa you are too low')
else:
    print('Aaaahaa you are too high')