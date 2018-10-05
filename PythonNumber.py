# Python Number
import math
import random

myList = [1, 10, 1.00]
print(type(myList[0]))

for i in myList:
	print(str(type(i)) + ", ", end = "")
print()

a = -4.3
b = 5.6
c = 6.7

# Mathematical Functions
List2 = [
			abs(a), 
			math.ceil(a), 
			math.exp(b), 
			math.fabs(a),
			math.floor(b),
			math.log10(c),
			max(a, b, c),
			math.pow(b, c),
			math.sqrt(b)
			]

print(List2)

# Random Number Functions
random.seed(10)
List3 = [
			random.choice([a, b, c]),
			random.choice("LearningPython."),
			random.random(),
			random.random(),
			random.uniform(10, 13)
]

print(List3)

# Trigonometric Functions
List4 = [
			math.sin(math.radians(30)),
			math.cos(math.radians(30)),
]
print(List4)

# Mathematical Constants
print(math.pi, math.e)