import random

s = 'QWERTYUIOPASDFGHJKLZXCVBNMmnbvcxzasdfghjklpoiuytrewq!@#$%^&*()?+/*'
n = int(input('Enter the size of password : '))
pas = ''.join(random.sample(s, n))

print('Your password : '+str(pas))