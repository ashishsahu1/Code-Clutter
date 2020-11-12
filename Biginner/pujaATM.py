#https://www.codechef.com/problems/HS08TEST

withdrawal_amount, balance_amount = input().split()              
withdrawal_amount = int(withdrawal_amount)                        
balance_amount = float(balance_amount)                            
if (withdrawal_amount % 5 == 0 and balance_amount>(withdrawal_amount+.5)):
    balance_amount = balance_amount - withdrawal_amount - 0.5     
    print('%.2f' % balance_amount)
else:
    print('%.2f' % balance_amount)