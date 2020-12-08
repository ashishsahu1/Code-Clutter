def highestNumberOfProdWeCanBuy(lst,k):
    lst.sort()
    ans=0
    i=0
    while(i<len(lst) and k>lst[i]):
        ans+=1
        k-=lst[i]
        i+=1

    return ans

lst = list(map(int,input().split()))
k = int(input())
print(highestNumberOfProdWeCanBuy(lst,k))