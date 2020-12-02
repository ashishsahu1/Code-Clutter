def removeDuplicates(arr, n): 
	if n == 0 or n == 1: 
		return n 
	j = 0

	for i in range(0, n-1): 
		if arr[i] != arr[i+1]: 
			arr[j] = arr[i] 
			j += 1

	arr[j] = arr[n-1] 
	j += 1
	return j 

# Driver code 
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5] 
n = len(arr) 

n = removeDuplicates(arr, n) 

for i in range(0, n): 
	print (" %d "%(arr[i]), end = " ") 
