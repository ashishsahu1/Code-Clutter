lst1 = list(map(int,input("First List : ").split()))
lst2 = list(map(int,input("Second List : ").split()))
outLst=[]

for i in lst1:
    if (i in lst2):
        if i in outLst:
            pass
        else:
            outLst.append(i)

print(outLst)