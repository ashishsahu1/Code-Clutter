def check(lst):
    for i in range(len(lst)):
        if lst[i]!=lst[-(i+1)]:
            return 1
    return 0
        

lst = list(map(int,input().split()))

if(check(lst)):
    print('Not Palindrome')
else:
    print('palindrome')    




