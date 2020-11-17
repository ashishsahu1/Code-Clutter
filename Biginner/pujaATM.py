#https://www.codechef.com/problems/HS08TEST

x, y = input().split()              
x = int(x)                        
y = float(y)                            
if (x % 5 == 0 and y>(x+.5)):
    y = y - x - 0.5     
    print('%.2f' % y)
else:
    print('%.2f' % y)