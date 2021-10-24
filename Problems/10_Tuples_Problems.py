# create a tuple form dictonary and then sort
Dict = {'Python': 5, 'Kubernetes': 5, 'Docker': 4, 'DevOps': 2, 'Terraform': 2}

tup = Dict.items()
sorted_tup = sorted(tup)
rev_sorted_tup = sorted(tup, reverse=True)
print(f'Original Tuple is : {tup}')
print(f'sorted in normal order : {sorted_tup}')
print(f'sorted in reverse order : {rev_sorted_tup}')

for k, v in sorted_tup:
    print(k, v)
