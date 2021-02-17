
def primeCheck(n):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,(n/2)+1):
            if n%i ==0:
                return False
                
    
            

n = int(input('Enter the number : '))
if primeCheck(primeCheck(int(n))):
    print('Prime')
else:
    print('Not Prime')