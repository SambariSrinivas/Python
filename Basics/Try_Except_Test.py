x = input("Enter a value for x: ")
try:
    x = int(x)
except:
    print(' Invalid Input Value entered for x')
    x = -1
if x >= 0:
    print('x is a positive number')
else:
    print('x is a Negative number')
