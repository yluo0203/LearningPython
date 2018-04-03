#10_BITWISE OPERATORS
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


#Slip and Slide
#Define a function called flip_bit that takes the inputs (number, n).
#Flip the nth bit (with the ones bit being the first bit) and store it in result.
#Return the result of calling bin(result).
def flip_bit(number, n):
  mask = 0b1
  mask = mask << (n - 1)
  result = (number ^ mask)
  return bin(result)