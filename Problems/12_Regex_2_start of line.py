import re

file = open("test_file.txt")
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
