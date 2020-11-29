s = "abcd"
n = len(s)
for i in range(1,n+1):
    for j in range(n-i+1):
        l = j+i-1
        for k in range(j,l+1):
            print(s[k],end="")
        print()