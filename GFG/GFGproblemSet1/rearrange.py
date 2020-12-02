def rearrange(arr, n): 
	for i in range(0, n): 
		arr[i] += (arr[arr[i]] % n) * n 
	for i in range(0, n): 
		arr[i] = int(arr[i] / n) 

def printArr(arr, n): 
	for i in range(0, n): 
		print (arr[i], end =" ") 
	print ("") 

for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    rearrange(arr, n); 
    printArr(arr, n) 

