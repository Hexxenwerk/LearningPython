from pprint import pprint

user = {"id": 1, "first_name": "Thomas", "last_name": "Meier"}
print(user, type(user))

# Alternative dictionary creation
user = dict(id=1, first_name='Thomas', last_name='Meier')
print(user, type(user))

# Add new key:value pair
user["location"] = "Hamburg"
print(user)

user["location"] = "Berlin"
pprint(user)

# Get a value of a key
print(user['location'])
# print(user['car'])  # None --> key does not exist

# Delete entry from dict
user.pop('location')
