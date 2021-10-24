num_list = list()
while True:
    inp = input("Enter the value : ")
    if inp.lower() == 'done':
        break
    else:
        value = float(inp)
        num_list.append(value)
average = sum(num_list) / len(num_list)
print(f'Average of all numbers are : {average}')
