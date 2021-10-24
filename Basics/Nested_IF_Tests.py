x = input("Enter the Value for x: ")
x = int(x)
if x > 0:
    print('x is greater than zero')
    if x > 100:
        print('x is greater than 100')
    elif x < 100:
        print('x is less than 100')
    else:
        print('x is equal to 100')
elif x < 0:
    print('x is less than zero and it is a negative number')
else:
    print('x is equals to zero')
