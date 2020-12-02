def rotateArr(A,D,N):
    tmp=[]
    for i in range(0,D):
        print(A[i])
        tmp.append(A[i])
        A.pop(i)
    
    for i in range(len(tmp)):
        A.append(tmp[i])

a = [1,2,3,4,5]
d=2
n=5
rotateArr(a,d,n)
print(a)