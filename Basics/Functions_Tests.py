# Testing Built in Functions Min and Max

big = max('Hello world')
print(big)
small = min('Hello world')
print(small)


# Custom Functions
# Adding two numbers

def addition(x, y):
    """this function is used to add two number"""
    print("We are adding " + str(x) + " and " + str(y) + "\n")
    return x + y


def subtraction(x, y):
    """This Function is used to subtract a number from another number """
    print("We are subtracting " + str(y) + " from " + str(x) + "\n")
    return x - y


Add = addition(3, 4)
Sub = subtraction(34, 18)

print('Addition of 3 and 4 is : ' + str(Add) + '\n')
print('subtraction of 34 and 18 is : ' + str(Sub) + '\n')

"""This is a multiline comment, starting with first line
here is the second line
this is the third and final line of the multiline comment."""
