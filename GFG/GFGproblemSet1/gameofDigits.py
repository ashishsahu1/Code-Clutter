import math as mt
# def smallx(n):
#     lst=[]
#     if len(str(n))==1:
#         return n
#     elif len(str(n))>1:
#         for i in range(1,math.floor(math.sqrt(n))+1):
#             if n%i==0:
#                 lst.append([i,n//i])
        
#         for i in range(len(lst)):
#             lst[i]= int(str(lst[i][0])+str(lst[i][1]))
#         return min(lst)
#     else:
#         return -1

    if (n >= 0 and n <= 9): 
        return n 
    digits = list() 
    for i in range(9,1, -1): 
        while (n % i == 0): 
            digits.append(i) 
            n = n //i 
    if (n != 1): 
        return -1
    k = 0
    while (len(digits) != 0): 
        k = k * 10 + digits[-1] 
        digits.pop() 
    return k
    

n=12
print(smallx(n))