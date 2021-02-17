import random

if(input('1.Input \n 2.Random') == 1):
    a = list(map(int,input('First list : ').split()))
    b = list(map(int,input('Second list : ').split()))
else:
    a = random.sample(range(1,50),10)
    b = random.sample(range(1,50),5)

ans = [] 
[ans.append(x) for x in a if x in b and x not in ans]
print(ans)