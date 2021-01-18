for i in range(int(input())):
    n ,k = input().split()
    n,k = int(n),int(k)
    lst = list(map(int,input().split()))

#Method 1***************************************************
#     temp=0
#     for i in range(k):
#         temp = lst[n-1]
#         for j in range(n-1,-1,-1):
#             lst[j]=lst[j-1]
#         lst[0]=temp
#     for i in range(n):
#         print(lst[i],end=' ')
#     print()

#Method 2****************************************************
    lst2 = lst[:n-k]
    lst3 = lst[n-k:n]
    lst = lst3+lst2
    print(lst)




