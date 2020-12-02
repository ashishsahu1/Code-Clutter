a = [0,-10,1,3,-20]

a.sort()
print(a)

for i in a:
    if int(a)<0:
        a.remove(i)

print(a)