def fib(n):
    a = 1
    b = 1
    count = 0
    fibLst = [a,b]
    while count!=n:
        fibLst.append(a+b)
        b = a+b
        a = b-a
        count+=1

    return fibLst


n = int(input('Enter the number : '))
print(fib(n))