# Python String
# Ref: https://www.tutorialspoint.com/python/python_strings.htm
# isVar = "Tony Lu"
# print(type(isVar))
# # <class 'str'>

# isNumber = 30
# print(type(isNumber))
# print(type(float(isNumber)))

isStr = "What doesn't kill you, makes you stronger."
# print(isStr)
# print(len(isStr))
# print(isStr[23: len(isStr)])
# print("What doesn't kill you," + isStr[23: len(isStr)])
# print(isStr[23].upper() + isStr[24: len(isStr)])

# Built-in String Methods
isStr2 = "google"
isDigit = "624"
isTodat = "Todayis10052018"
isList = [
			isStr2.capitalize(),
			isStr2.center(10, "X"),			# XXgoogleXX
			isStr2.count("o", 0, len(isStr2)),
			isStr2.find("o"),
			isStr.endswith("you"),			# False
			isStr.endswith("stronger."), 	# True
			isStr.index("you"),				# 18
			isStr.index("you", 19),			# 29
			isDigit.isdigit(),				# True
			isStr.islower(),				# Fasle
			isTodat.isnumeric(),			# False
			isDigit.isnumeric(),			# True
			len(isStr),
			isStr.upper(),
			isStr.lstrip("What doesn't kill you, "),
			max(isStr),						# 'y'
			min(isStr),						# ''
			isStr.split(),
			isStr.split('y', 1)
		]

print(isList)