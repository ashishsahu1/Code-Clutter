for _ in range(int(input())):
    n,k = input().split()
    n,k = int(n),int(k)
    lst = map(int,input().split())
    l = k - min(lst)
    if(l<0):
        l= 0 
    print(l)
        
