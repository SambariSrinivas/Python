import xml.etree.ElementTree as ET

input_data = '''<stuff>
<users><user x="2">
<id>234</id>
<name>srini</name>
</user>
<user x="23">
<id>678</id>
<name>tej</name>
</user>
</users>
</stuff>'''

parsed_data = ET.fromstring(input_data)
print(type(parsed_data))
users = parsed_data.findall('users/user')
print(type(users))
print(users)
print(f'users count is : {len(users)}')
for user in users:
    print(type(user))
    print(f'Name : {user.find("name").text}')
    print(f'Id : {user.find("id").text}')
    print(f'Attribute : {user.get("x")}')
