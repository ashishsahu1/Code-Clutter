n,h,x = input().split()
lstT = map(int,input().split())
ans = False
for i in lstT:
    if int(x)+i==int(h):
        ans = True

if ans == True:
    print('Yes')
else:
    print('No')
