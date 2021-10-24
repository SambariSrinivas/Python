list = [2, 45, 34, 98, 45, 6, 9, -124, 23, -2, -4]


def find_large_num():
    large_num = None
    for num in list:
        if large_num is None or num > large_num:
            large_num = num
    print(f'Largest Num in the list is : {large_num}')


def find_smallest_num():
    smallest_num = None
    for num in list:
        if smallest_num is None or num < smallest_num:
            smallest_num = num
    print(f'Smallest Num in the list is : {smallest_num}')


find_large_num()
find_smallest_num()
