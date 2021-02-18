#using linear search
def search1(x, lst):
    for i in range(len(lst)):
        if lst[i]==x:
            return i+1
    return 'something wrong'

#using function
def search2(x, lst):
    return lst.index(x)+1

#binary search
def search3(x, lst,s,e):
    lst.sort()
    n = len(lst)
    mid = (s+e)//2
    if lst[mid]==x:
        return mid+1
    elif lst[mid]>x:
        return search3(x,lst, s,mid+1)
    else:
        return search3(x,lst,mid-1,e)

lst = list(map(int,input('Enter the List : ').split()))
x = int(input('Enter the element :'))
print(search1(x, lst))
print(search2(x, lst))
print(search3(x, lst, 0 ,len(lst)-1))
