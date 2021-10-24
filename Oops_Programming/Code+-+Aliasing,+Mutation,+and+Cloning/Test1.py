import copy

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = copy.deepcopy(a)
c = copy.deepcopy(b)
b = copy.deepcopy(c)


def remove_elem(data, target):
    for item in data.copy():
        if item == target:
            data.remove(target)
    return data


def get_product(data):
    total = 1
    for i in range(len(data.copy())):
        total *= data.pop()
    return total


remove_elem(c, 3)
print(get_product(b))
print(a)
