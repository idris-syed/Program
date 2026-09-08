n= int(input('enter a value:'))

if n%3==0 and n%5==0:
    print('Divisible by both 3 and 5')
elif n%3==0:
    print('Divisible by 3')
elif n%5==0:
    print('divisible by 5')
else:
    print('not divisible by both')
    