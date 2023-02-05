person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the spouse
print(person["spouse"])

# print out the name of the second child
print(person["children"][1])

# print out the name of the cat
print(person["pets"]["cat"])

# use a loop to print out the names of the each child
for name in person["children"]:
    print(name)

# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
for key, value in person["pets"].items():
    print(f"The type of pet is: {key} and the name of the pet is: {value}")

dict_pets = person["pets"]
for key in dict_pets:
    print(f"The type of pet is: {key} and the name of the pet is: {dict_pets[key]}")
