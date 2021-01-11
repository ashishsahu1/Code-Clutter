def check(s):
    lst = []
    for i in range(len(s)):
        if s[i]=='(':
            lst.append(s[i])
        if s[i]==')':
            if len(lst)!=0:
                lst.pop()
    if len(lst)==0:
        return True
    else: 
        return False

s = input()
c=0
for i in range(len(s)):
    sl = ''
    for j in range(i,len(s)):
        sl = sl+s[j]
    for k in range(i):
        sl = sl+s[k]
    if check(sl):
        c+=1
print(c)
