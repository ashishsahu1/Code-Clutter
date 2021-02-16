x = int(input("Enter the number : "))

# Method1 : remainder
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")

#method2 : bitwise
if x&1 == 1:
    print("Odd")
else:
    print("Even")