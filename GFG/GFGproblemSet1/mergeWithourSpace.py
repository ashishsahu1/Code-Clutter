a = [1,3,5,7]
b = [0,2,6,8,9]
an = len(a)
bn = len(b)

a[len(a):] = b
a.sort()
print(a,b,an,bn)
b.clear

for i in range(an,an+bn):
    print(a[i])
    b.append(a[i])
   

    
print(a,b,an,bn)