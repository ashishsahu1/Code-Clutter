# for _ in range(int(input())):
#     c = int(input())
#     lst=[]
#     v = 2**(len(bin(c))-2)
#     for i in range(1,v):
#         for j in range(v,0,-1):
#             if i^j==c:
#                 lst.append(i*j)

#     print(max(lst))


# for _ in range(int(input())):
#     c = int(input())
#     a = 2**(len(bin(c))-2)
#     b = c^a
#     print(a*b,a,b,c)

for _ in range(int(input())):
    c = int(input())
    temp = c
    i=0
    while(temp>0):
        temp = temp//2
        i+=1

    a = 2**(i-1)

    b = a^c

    print(a*b,a,b)