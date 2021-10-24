"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

a = [1, 2, 3, 4]
b = a

b[0] = 15

print(a)
print(b)

x = [1, 2, 3, 4, 5]
print('Before Mutation id of x is : ', id(x))
print(x)
x[0] = 10
print('After Mutation id of x is : ', id(x))
print(x)