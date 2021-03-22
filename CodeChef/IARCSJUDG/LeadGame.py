n = int(input())
p1=[]
p2=[]
for _ in range(n):
    x,y = input().split()
    p1.append(int(x))
    p2.append(int(y))
# win = n*[0]
maxScore=0
player = 0
for i in range(n):
    if p1[i]>p2[i]:
        if p1[i]-p2[i]>maxScore:
            maxScore = p1[i]-p2[i]
            player = 1
    else:
        if p2[i]-p1[i]>maxScore:
            maxScore = p2[i]-p1[i]
            player = 2

print(player, maxScore)
