import random

while True:
    a = random.randint(1,9)
    x = input('Gues the number : ')

    if x=='exit':
        break

    if x==a:
        print('Damn, you guessed it right')
    elif x<a:
        print('Aaaahaa you are too low')
    else:
        print('Aaaahaa you are too high')