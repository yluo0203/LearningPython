# Python Decision MakingAndLoops
# import random
# import calendar

for i in range(1, 30):
	if (i % 3 == 0 and i % 5 == 0):
		print("FizzBuzz, ", end = "")
	elif (i % 3 == 0):
		print("Fizz, ", end = "")
	elif (i % 5 == 0):
		print("Buzz, ", end = "")
	else:
		print(str(i) + ", ", end = "")
print()

i = 0
while i < 30:
	i += 1
	if (i % 3 == 0 and i % 5 == 0):
		print("FizzBuzz, ", end = "")
	elif (i % 3 == 0):
		print("Fizz, ", end = "")
	elif (i % 5 == 0):
		print("Buzz, ", end = "")
	else:
		print(str(i) + ", ", end = "")
print()


def UpperLetter(char):
	print(char.upper() + ' ', end = '')

for c in "LearningPython.":
	UpperLetter(c)
print()

# List Comprehensions in Python
newList = [c.upper() for c in "LearningPython."]
print(newList)