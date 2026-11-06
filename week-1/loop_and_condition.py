# Exercise: Pass or fail
marks = 67
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Exercise: Grade calculator
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)

# Exercise: Print numbers and their squares
for number in range(1, 6):
    print(number, "squared =", number ** 2)

# Exercise: Sum using a while loop
number = 1
total = 0
while number <= 10:
    total += number
    number += 1
print("Sum from 1 to 10:", total)

# Exercise 12: List comprehension - even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

