def search1(x, lst):
    for i in range(len(lst)):
        if lst[i]==x:
            return i+1
    return 'something wrong'

def search2(x, lst):
    return lst.index(x)+1

def search2(x, lst):
    lst.sort()
    

lst = list(map(int,input('Enter the List').split()))
x = int(input('Enter the element :'))
print(search1(x, lst))
print(search2(x, lst))
