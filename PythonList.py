# Python List
# Red: https://www.tutorialspoint.com/python/python_lists.htm

ListElbert = ["Life", "Is", "Like", "Riding", "a", "Bicycle.", "To", "Keep", "Your", "Balance", "You", "Must", "Keep", "Moving"]
ListNumbers = [1, 3, 5, 6, 7, 9, 14, 17, 19, 22, 24]
ListTony = ["stay", "hungry"]

print("ListElbert[0]: " + ListElbert[0])
print(ListNumbers[1: 4])
print()

# Updating Lists
ListNumbers[0] = 2
print(ListNumbers[0: 3])
ListNumbers.append(25)
print(ListNumbers)
print()

# Delete List Elements
del ListNumbers[11]
print(ListNumbers)
print()

# Basic List Operations
print(len(ListNumbers))
print(ListNumbers + ListElbert)
print(24 in ListNumbers)
print(["Z"] * 4)
print()

#Indexing, Slicing, and Matrixes
print(ListElbert[3])
print(ListElbert[-3])
print(ListElbert[1:])
print()

# Built-in List Functions & Methods
print(max(ListElbert))

# Methods with Description
ListTony.append("stay")
ListTony.append("foolish")
print(ListTony)

print(ListTony.count("stay"))
ListTony.extend(ListElbert)
print(ListTony)
print(ListTony.index("Life"))
ListTony.insert(11, ListNumbers)
print(ListTony)

print(ListTony.pop(10))
print(ListTony)

for i in range(1, 14):
	print(ListTony.pop())

ListTony.remove("Life")
print(ListTony)

ListNumbers.reverse()
print(ListNumbers)
ListNumbers.sort()
print(ListNumbers)
ListTony.sort()
print(ListTony)






