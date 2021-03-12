for i in range(int(input())):
    s = input()
    C=0
    if s[0]=='1':
        C=1
    for i in range(len(s)-1):
        if s[i]=='0' and s[i+1]=='1':
            C+=1

    print(C)