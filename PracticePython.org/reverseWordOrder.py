def rev(str):
    strLst = list(str.split())
    # strLst2 = strLst[-1::-1]
    
    return ' '.join(strLst[-1::-1])


str = input()
print(rev(str))