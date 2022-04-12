import json 

with open("some_file_json.json", "r") as json_file:
    file_data = json_file.read()
    dict1_from_file = json.loads(file_data)
    # json.dumps(json_file)
# print(dict1_from_file)


with open("some_file_json.json", "w") as new_json:
    new_json.write(json.dumps(dict1_from_file))
    print(new_json)