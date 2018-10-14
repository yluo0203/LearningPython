# Python Dictionary
# Ref: https://www.tutorialspoint.com/python3/python_dictionary.htm

dict1 = {}
# print(type(dict1))

dict2 = dict()
# print(type(dict2))

dict1["Name"] = "Elsa"					
dict1["Grades"] = [90, 80, 88, 79]		
print(dict1["Name"])					# Elsa
print(dict1["Grades"])					# [90, 80, 88, 79]
print(dict1["Grades"][0])				# 90

dict1 = {"Birthday": "0606", "PhoneNumebr": "123456789"}
print(dict1["Birthday"])				# 0606
print(dict1)							# {'PhoneNumebr': '123456789', 'Birthday': '0606'}

# print(dict1["Name"])					# There is no "Name" and "Grades" exist.
Tony = ["TonyLu", [90, 80, 88, 79], "0203", "123456789"]
dict2["Name"] = Tony.pop(0)				
print(dict2["Name"])					# TonyLu
dict2["Grades"] = Tony.pop(0)
print(dict2["Grades"])					# [90, 80, 88, 79]
print(dict2["Grades"][0:2])				# [90, 80]

dict3 = {"a": "apple", "b": "banana", "c": "cat"}
print(dict3["a"])
dict3["a"] = "abandon"
print(dict3["a"])

# Delete Dictionary Elements
del dict3["c"]
print(dict3)
dict3.clear();
print(dict3);
# del dict3;
# print(dict3)
dict3 = {"a": "apple", "b": "banana", "c": "cat"}

# Built-in Dictionary Functions & Methods
# cmp(dict1, dict3)						# No longer available in Python 3.
print(len(dict3))
print(str(dict3))
print(type(dict3))

# Method & Description
dictCopy = dict3.copy()
print(dictCopy)

theKeys = ("apple", "banana", "orange")
dictFruit = dict.fromkeys(theKeys)
print(dictFruit)

dictFruit = dict.fromkeys(theKeys, 10)
print(dictFruit)

print(dictFruit.get("apple"))
# print(dictFruit.has_key("apple"))		# Removed, use the in operation instead.

print(dictFruit.items())
print(dictFruit.keys())


dictFruit.setdefault("garpes", 20)
print(dictFruit)

dict1.update(dictFruit)
print(dict1)

print(dict1.values())
















