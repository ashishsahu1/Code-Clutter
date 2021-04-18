for _ in range(int(input())):
    lst = list(map(int,input().split()))
    st = dict(zip(list(set(lst)),range(len(lst))))
    print(st,lst)
    # for i in range(len(lst)):