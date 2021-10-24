name = 'sRiniVaS'
surname = "sambari"
print(name)
print(name.lower())
print(name.upper())
print(name.capitalize())
print(len(name))
print(isinstance(name, str))
print(name[2])
print(type(name))
print(name.find('a'))

print("============= String Slicing =================")

print(name[2:5])
print(name[:4])
print(name[3:].lower())

print("============ String concatination ===============")
print(name.capitalize() + ' ' + surname.capitalize())

line = "Hello! Where are you all"
print(line.split())  # split converts the string into list of strings by taking space or specified delimeter
print(len(line.split()))
