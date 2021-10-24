import re

file = open('Regex-3-data-file.txt')

for line in file:
    if re.search('^X.*:', line):  # regex ^X.*:  --> suites for example X-data:
        print(line.rstrip())

print("============= Excluding the whitespaced lines in regex ==============")

for line in file:
    if re.search("^X-\S+:", line):
        print(line.rstrip())
