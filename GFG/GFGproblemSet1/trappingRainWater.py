#trapping rain water problem

def maxLft(lst, i):
    max = lst[i]
    for j in range(i,-1,-1):
        if lst[j]>max:
            max = lst[j]
    return max

def maxRt(lst,i):
    max = lst[i]
    for j in range(i,len(lst)):
        if lst[j]>max:
            max = lst[j]
    return max

def min(x,y):
    if x<y:
        return x
    else:
        return y

lst = list(map(int,input().split()))
print(lst)
sum = 0
for i in range(len(lst)):
    x = maxLft(lst,i)
    y = maxRt(lst,i)
    z = min(x,y)
    sum = sum+(z-lst[i])

print(sum)