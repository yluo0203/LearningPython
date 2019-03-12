# swap_list_element.py

list = ["a", "b", "c", "d", 0, 0.1, 0.2, 1, 1.1, 1.2, 2, 2.1, 2.2, 3, 3.1, 3.2, 4, 4.1, 4.2, 5, 5.1, 5.2, 6, 6.1, 6.2]
start = 4
end = len(list) - 1
print(start, end)

def print_element():
  for i in range (start, end + 1):
    print list[i]
    pass

lhs = start
rhs = end
while lhs + 1 < rhs:
  list[lhs], list[rhs] = list[rhs], list[lhs]
  lhs += 1
  rhs -= 1
# print_element()
# print(lhs, list[lhs], rhs, list[rhs])
# while 
for i in range(start, end + 1, 3):
  list[i], list[i + 2] = list[i + 2], list[i]
print_element()