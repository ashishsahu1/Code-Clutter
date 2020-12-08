def binary(lst, k, n):
    l = 0
    r = n-1
    while(l <= r):
        m = (l+r)//2
        if(lst[m] == k):
            return m
    
        if(lst[m] < k):
            l = m+1
        else:
            r = m-1
    return -1


lst = [1, 4, 5, 7, 21, 12, 13, 98]
k = 7
n = len(lst)
lst.sort()

result = binary(lst, k, n)
if(result != -1):
    print("Element is not present")
    
else: 
    print("Present")