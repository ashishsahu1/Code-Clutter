lst1= list(map(int,input().split()))
lst2= list(map(int,input().split()))
diff = abs(sum(lst2) - sum(lst1))
# print(diff)
lstT=[]
prodE = []
prodO = []
elE = []
elO = []
lstT1 = lst1.copy()
lstT2 = lst2.copy()
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if abs(lst1[i]-lst2[j])==diff//2:
            if lst1[i] in lstT1 and lst2[j] in lstT2:
                if (lst1[i]*lst2[j])%2==0:
                    prodE.append(lst1[i]*lst2[j])
                    elE.append((lst1[i],lst2[j]))
                else:
                    prodO.append(lst1[i]*lst2[j])
                    elO.append((lst1[i],lst2[j]))
                lstT1.remove(lst1[i])
                lstT2.remove(lst2[j])

while(len(prodE)!=0):
    x = prodE.index(min(prodE))
    t = elE[x]
    for i in t:
        lstT.append(i)
    prodE.pop(x)
    elE.pop(x)

while(len(prodO)!=0):
    x = prodO.index(max(prodO))
    t = elO[x]
    for i in t:
        lstT.append(i)
    prodO.pop(x)
    elO.pop(x)

m = -1
if len(lstT)==0:
    print(m)
else:   
    c_list = [str(element) for element in lstT]
    st = ",".join(c_list)
    print(st)
