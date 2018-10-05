# Python Operators

# Arithmetic Operators
calculate = 3 * 3
print(calculate)	# 9

calculate = 2345 / 321
print(calculate)	# 7.305295950155763

calculate = 2345 // 321
print(calculate)	# 7

calculate = 2345 % 321
print(calculate)	# 98

calculate2 = 2345 ** 321
# print(calculate2)	# 654...625
# print(type(calculate2)) # <class 'int'>

# Python Comparison Operators
a = 20 
b = 90
print(a == b)

# Python Bitwise Operators
bin_a = bin(a)
bin_b = bin(b)
print(type(bin_b))	# <class 'str'>
print(bin_a, bin_b)	# 0b10100 0b1011010
print(bin(a & b))	# 0b10000

# print(bin_a | bin_b)
print(a | b)
# print(bin_a ^ bin_b)
print(a ^ b)

print(bin(b << 2))
