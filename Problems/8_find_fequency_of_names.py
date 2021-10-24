skills = ['Python', 'Kubernetes', 'Python', 'Kubernetes', 'Docker', 'DevOps', 'Terraform'
    , 'Python', 'Kubernetes', 'Docker', 'Python', 'Kubernetes', 'Docker', 'DevOps', 'Terraform', 'Python',
          'Kubernetes', 'Docker']

count = dict();
count2 = dict();
for skill in skills:
    if skill in count:
        count[skill] = count[skill] + 1
    else:
        count[skill] = 1

print(f"Frequency from first dictionary : {count}")

for skill in skills:
    count2[skill] = count2.get(skill, 0) + 1

print(f"Frequency from second dictionary : {count2}")
