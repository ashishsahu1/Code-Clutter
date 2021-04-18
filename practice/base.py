import math


def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current//n
    return new_num_string

def maxRepeating(str1, str2):

    cntOcc = str1.count(str2)
    Contstr = str2 * cntOcc
    while(Contstr not in str1):
        cntOcc -= 1
        Contstr = str2 * cntOcc
         
    return cntOcc

n = int(input())
b = int(input())

st = base10toN(n,b)
str2='0'
c = maxRepeating(st,str2)
if c==0:
    print('-1')
else:
    print(c)