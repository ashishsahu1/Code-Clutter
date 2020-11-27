lst=[]
for _ in range(int(input())):
    lst = [int(x) for x in input()]
    print(lst[0]+lst[len(lst)-1])

# for i in range(int(input())):
#     n = int(input())
#     ld = n%10
#     print(ld)
#     while n>0:
#         n = n//10
#     fd = n
#     print(fd)
#     print(ld+fd)