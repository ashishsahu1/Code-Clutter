import random

def getCowBull(gen,guess):
    cow , bull = 0,0
    
    for i in range(4):
        if gen[i]==guess[i]:
            cow+=1
        else:
            bull+=1
    if cow == 4:
        return 'You won'
    return 'Cow : '+str(cow)+' and Bull : '+str(bull)

genN = random.randint(1000,9999)
genLst = []
[genLst.append(n) for n in str(genN)]
print('Number generated')
while True:
    guessN = input('Try your guess : ')
    guessLst = []
    [guessLst.append(n) for n in guessN]

    print(getCowBull(genLst,guessLst))
    if getCowBull(genLst,guessLst)=='You won':
        break
