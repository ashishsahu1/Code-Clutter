#check weather no is prime or not

import math
def isprime(n):
    if n<2:
        return "not prime"

    for i in range(2,(math.floor(math.sqrt(n)))+1):
        if n%i==0:
            return "not prime"

    return "prime"
            


if __name__ == "__main__":
    n = int(input('Enter your number : '))
    print(isprime(n))

