n = int(input())
tempDiv = list(range(1,n+1))
finDiv = []
for i in tempDiv:
    if n%i == 0:
        finDiv.append(i)
print(finDiv)
