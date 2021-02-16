lst = map(int,input().split())
lst2=[]
# for i in lst:
#     if i<5:
#         lst2.append(i)

#using list comprehension
[lst2.append(ax) for ax in lst if ax<5]
print(lst2)