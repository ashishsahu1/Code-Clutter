# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

#driver code
a = list(map(int,input("Enter the list : ").split()))
b = []
b = [aa for aa in a if aa%2==0]
print(b)