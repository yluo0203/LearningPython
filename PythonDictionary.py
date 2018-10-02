# Python Dictionary
dict1 = {}
# print(type(dict1))

dict2 = dict()
# print(type(dict2))

dict1["Name"] = "Elsa"
dict1["Grades"] = [90, 80, 88, 79]
print(dict1["Name"])
print(dict1["Grades"])
print(dict1["Grades"][0])

dict1 = {"Birthday": "0606", "PhoneNumebr": "123456789"}
print(dict1["Birthday"])
print(dict1)

# print(dict1["Name"])					# There is no "Name" and "Grades" exist.
Tony = ["TonyLu", [90, 80, 88, 79], "0203", "123456789"]
dict2["Name"] = Tony.pop(0)
print(dict2["Name"])
dict2["Grades"] = Tony.pop(0)
print(dict2["Grades"])
print(dict2["Grades"][0:2])