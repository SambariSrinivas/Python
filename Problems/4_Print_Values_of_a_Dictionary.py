print("================ Dictionary One ========================")
dict1 = {'Name': 'Srinivas Sambari', 'Age': 33, 'Role': 'QA-Engineer', 'Experience': 11.25}
for key in dict1:
    print(f'{key} : {dict1[key]}')

print("================ Now Dictionary Two ========================")
dict2 = dict()
dict2['Name'] = "Ravi Teja"
dict2['WorkLocation'] = "Chennai"
dict2['Company'] = "HCL"
dict2['Skills'] = ["Python", "Kubernetes", "Docker", "DevOps", "Terraform"]


for key in dict2:
    print(f'{key} : {dict2[key]}')
