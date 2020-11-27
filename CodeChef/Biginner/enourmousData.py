#https://www.codechef.com/problems/INTEST

n,k = map(int,input().split())
lst =[]
c=0
for i in range(n):
    lst.append(int(input()))

for i in range(n):
    if lst[i]%k ==0:
        c+=1

print(c)