def remDuplicate(lst):
    ls = []
    for i in lst:
        if i not in ls:
            ls.append(i)
    return ls

def remDuplicate2(lst):
    ls = []
    [ls.append(x) for x in lst if x not in ls]
    return(ls)

def remDuplicate3(lst):
    return list(set(lst))

lst = list(map(int,input("Enter the list : ").split()))
print(remDuplicate(lst))
print(remDuplicate2(lst))
print(remDuplicate3(lst))