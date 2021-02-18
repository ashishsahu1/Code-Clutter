'''
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---
'''

def horiz(n):
    for i in range(n):
        print(' ---',end="")
    print()

def vert(m):
    for i in range(m+1):
        print('|   ',end="")
    print()


n = int(input('Enter the size of pattern : '))
for i in range(n):
    horiz(n)
    vert(n)

horiz(n)