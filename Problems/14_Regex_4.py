import re

line1 = "From Stephan.marqued@uct.ac.za Sat Jun 04 14:23:29 2021"
line2 = "To marko.taükeßn@ben.ucb.in Tue Jul 09 12:09:33 2020"
from_address = re.findall('\S+@\S+', line1)
print(from_address)

to_address = re.findall('\S+?@\S+?', line2)
print(to_address)
