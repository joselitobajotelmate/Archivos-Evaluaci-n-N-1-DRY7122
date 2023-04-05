import json


with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as f:
    json_file = json.load(f)


print(json_file)