#10_ADVANCED TOPICS IN PYTHON

#lambda expressions
#Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

#Iterating Over Dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

#dictionary methods: https://www.tutorialspoint.com/python/python_dictionary.htm
print movies.items()

#Comprehending Comprehensions
#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [
  x for x in range(1,16) if (x % 3 == 0 or x % 5 == 0)
]

#List Slicing / Lambda Expressions
#The string in the editor is garbled in two ways: 1. Our message is backwards. 2. The letter we want is every other letter.
#Use list slicing to extract the message and save it to a variable called message
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
message = filter(lambda i: i != "X", message)
print messages
# "I am another secret message!"