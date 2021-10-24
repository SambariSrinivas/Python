fruit = 'apple'
print(fruit)
print('Orange')
print(fruit[4])
fruit_length = len(fruit)
print(fruit_length)

print(fruit.upper())
print((fruit.upper()).capitalize())

print('I' + ' Love ' + fruit.capitalize())

print(fruit + ' is mine')

version = 3

print('I' + ' Love ' + 'Python' + str(version))
print('{1} {0} '.format('Srinivas', 'Sambari'))
print('{0} {1}, {1} {0}'.format('Srinivas', 'Sambari'))

print('{0:8} | {1:<.2f}'.format('Apple', 2.994538))  # this is for formatting with floating number
print('{0:8} | {1:>.2f}'.format('Orange', 10))
