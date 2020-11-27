lstp1 = []
lstp2 = []
lstc = []
n = int(input())
for _ in range(n):
    p1,p2 = input().split()
    lstp1.append(int(p1))
    lstp2.append(int(p2))
#print(lstp1)
#print(lstp2)

for i in range(n):
    lstc.append(lstp1[i]-lstp2[i])
#print(lstc)

if abs(max(lstc))>abs(min(lstc)):
    if max(lstc)>0:
        print('1 '+str(abs(max(lstc))))
    else:
        print('2 '+str(abs(min(lstc))))