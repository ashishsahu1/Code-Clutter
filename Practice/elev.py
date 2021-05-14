def elev(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return sum(lst[:i])
    return elev(lst[:len(lst)-1])

lst = list(map(int, input().split()))
lst.sort()
print(elev(lst))