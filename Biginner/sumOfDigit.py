#https://www.codechef.com/problems/FLOW006

n = int(input())
for i in range(n):
    sum = 0
    x = int(input())
    while(x>0):
        sum = sum+x%10
        x = x//10
    
    print(sum)