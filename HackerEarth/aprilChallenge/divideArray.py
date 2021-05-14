def divArr(lst,n):
    c=-1
    for i in range(n):
        temp1 = lst[:i]
        temp2 = lst[i:]
        x=True
        while(x):
            c+=1
            if c not in temp1 and c not in temp2:
                return c
    return '-1'


for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    if (divArr(lst,n)==0 or divArr(lst,n)=='-1'):
        print('-1')
    else:
        print(divArr(lst,n))