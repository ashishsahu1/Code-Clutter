while True:
    
    x = input('Want to continue to play ? ')
    if x=='no':
        break

    cmdPlayer1 = input("Player1, Enter your choice : ")
    cmdPlayer2 = input("Player2, Enter your choice : ")
    if cmdPlayer1==cmdPlayer2:
        print("Draw")
    elif cmdPlayer1=='rock':
        if cmdPlayer2=='scissor':
            print('player 1 wins')
        else:
            print('player 2 wins')
    elif cmdPlayer1=='scissor':
        if cmdPlayer2=='paper':
            print('player 1 wins')
        else:
            print('player 2 wins')
    elif cmdPlayer1=='paper':
        if cmdPlayer2=='rock':
            print('player 1 wins')
        else:
            print('player 2 wins')

    
