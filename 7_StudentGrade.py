#Student Grade
#Ref: code cademy

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  result = float(total) / len(numbers) 
  return result

def get_average(student):
  homework = average(student["homework"])
  quizze = average(student["quizzes"])
  tests = average(student["tests"])
  result = 0.1 * homework + 0.3 * quizze + 0.6 * tests
  return result

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
    
#print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  avg = average(results)
  return avg

#1.Create a list called students and fill it with the three students, alice, lloyd, and tyler.
students = [alice, lloyd, tyler]

#2.Find the average grade of the class. Print this numerical grade to the terminal.
print get_class_average(students)

#3. Finally, determine the letter grade for the class's average and print it to the terminal.
print get_letter_grade(get_class_average(students))
