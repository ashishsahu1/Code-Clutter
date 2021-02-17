import math

def primeCheck(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
            # else:
        return True
    else:
        return False

def primeCheck2(n):
    if n<=1:
        return False
    if n<=3:
        return True
    
    for i in range(2,(math.ceil(math.sqrt(n)))+1):
        if n%i==0:
            return True
    
    return True

      

n = int(input('Enter the number : '))
if primeCheck(int(n)):
    print('Prime')
else:
    print('Not Prime')

if primeCheck2(int(n)):
    print('Prime')
else:
    print('Not Prime')


