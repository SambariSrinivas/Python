import json

input_data = '''{
  "name": "Chuck",
  "phone": {
    "type": "intl",
    "number": "+1 734 303 4456"
  },
  "email": {
    "hide": true
  }
}'''

info = json.loads(input_data)
print(type(info))
print(f'Dictionary length is : {len(info)}')
print(f'Name : {info["name"]}')
print(f'Hide_Email : {info["email"]["hide"]}')
print(f'Phone_Number : {info["phone"]["number"]}')
