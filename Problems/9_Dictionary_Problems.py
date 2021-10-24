Dict = {'Python': 5, 'Kubernetes': 5, 'Docker': 4, 'DevOps': 2, 'Terraform': 2}

for key in Dict:
    print(f'{key} has come {Dict[key]} times')

print("============================= Now in different way =========================")
for key, value in Dict.items():
    print(f'{key} has come {value} times')

print("============================= Dictionary Items =========================")
print(Dict.items())
