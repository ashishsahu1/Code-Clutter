#https://www.codechef.com/problems/FCTRL2


#********recursive*******
def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

for _ in range(int(input())):
    x = int(input())
    print(fact(x))

#******iterative*********
# def fact(x):
#     prod = 1
#     for i in range(1,x+1):
#         prod = prod*i
#     return prod

# for _ in range(int(input())):
#     x = int(input())
#     print(fact(x))

