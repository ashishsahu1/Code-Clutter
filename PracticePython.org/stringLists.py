'''
************Number palindrome check using loop***********************
'''

# def check(lst):
#     for i in range(len(lst)):
#         if lst[i]!=lst[-(i+1)]:
#             return 1
#     return 0
        

# lst = list(map(int,input().split()))

# if(check(lst)):
#     print('Not Palindrome')
# else:
#     print('palindrome')    

'''
************Word palindrome check***********************
'''

word = input("Enter the word : ")
revWord = word[::-1]
if word==revWord:
    print('palindrome')
else:
    print('not palindrome')



