def fact(num):
	fact = 1;
	while(num>1):
		fact = fact * num;
		num = num-1;
	return fact;

def catalan(n):
	return fact(2 * n)//(fact(n)*fact(n + 1))

if __name__ == '__main__':

	arr = list(map(int, input().split()))
    n = len(arr)
	s = 0
	for i in range(n):
		if arr[i] < arr[0]:
			s+= 1
	catalan_leftBST = catalan(s)
	catalan_rightBST = catalan(n-s-1)
	totalBST = catalan_rightBST * catalan_leftBST
	print(totalBST)
