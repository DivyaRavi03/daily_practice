import json

def describe_users(file):
    output = []
    user = ""
    with open(file, 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        person = data[i]
        name = person["name"]
        city = person.get("city", "Unknown")
        user = name + " (" + city + ")" 
        output.append(user)
    return output
users = [
    {"name": "Asha", "city": "Detroit"},
    {"name": "Ben"},
    {"name": "Chen", "city": "Austin"},
]
with open("users.json", "w") as f:
    json.dump(users, f)

print(describe_users("users.json"))  

with open("empty.json", "w") as f:
    json.dump([], f)

assert describe_users("users.json") == ["Asha (Detroit)", "Ben (Unknown)", "Chen (Austin)"]
assert describe_users("empty.json") == []

print("All tests passed!")    