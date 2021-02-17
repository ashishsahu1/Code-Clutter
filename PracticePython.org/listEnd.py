def listEnd(lst):
    ls = []
    ls.append(lst[0])
    ls.append(lst[-1])
    return ls

lst = list(map(int,input().split()))
print(listEnd(lst))