def maxaggregate(l):
    d = {}
    for i in l:
        d[i[0]] = 0
    for i in l:
        if i[0] in d:
            d[i[0]]+=i[1]
    max_key = max(d, key=d.get)
    return(max_key)
    
l = [('kohli',73),('ashwin',33),('kohli',7),('pujara',22),('ashwin',47)]
print(maxaggregate(l))