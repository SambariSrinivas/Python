# In python objects are passed to functions/methods by object reference only.

mylist = [3, 2, 4, 6]


def multiply_by_two(seq):
    print('Inside the function: ', id(seq))
    for i in range(len(seq)):
        seq[i] *= 2


print('Before multiplication : ', mylist)
print('Outside the function: ', id(mylist))
multiply_by_two(mylist)
print('After multiplication : ', mylist)
