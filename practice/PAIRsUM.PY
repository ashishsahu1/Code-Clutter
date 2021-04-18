def pairSum(n,lst):
    lst.sort()
    c=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==n:
                c+=1

    return c


n = int(input("Enter the number : "))
lst = list(map(int,input("Enter the list : ").split()))

print(pairSum(n,lst))