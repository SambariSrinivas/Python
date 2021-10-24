line = "Hello! Where are you all"
print(line.split())  # split converts the string into a list of strings by taking a delemiter as input
print(len(line.split()))

new_line = "Srini;Samba;Raikal;Hyderabad ;India"
new_list = new_line.split(';')
print(new_list)
print(new_list[3])