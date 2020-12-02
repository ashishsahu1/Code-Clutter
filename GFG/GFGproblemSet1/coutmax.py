def count(arr,n):
    c=0
    for i in range(len(arr)):
        if arr[i]==n:
            c+=1
    return c

def majorityWins(arr, n,  x,y):
    return (max(count(arr,x),count(arr,y)))


arr = [40,85 ,9 ,14 ,53]
x = 13
y=32
majorityWins(arr,len(arr),x,y)

print(x in arr)