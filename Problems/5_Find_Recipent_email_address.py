file = open("test_file.txt")
for line in file:
    if line.startswith("To:"):
        # print(line[:-1]) # here we are slicing the line by removing the last character.
        print(line.rstrip())  # rstring will remove the trailing character from right
        # print(line) # This will add a extra new line in the output window
