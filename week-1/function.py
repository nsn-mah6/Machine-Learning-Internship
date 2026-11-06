# Exercise: Function to calculate average
def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)

marks = [80, 75, 90, 85]
print("Average:", calculate_average(marks))

# Exercise: Function to find the largest of three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)

print("Largest:", largest_of_three(12, 45, 31))

# Exercise: Student result function
def get_result(name, score):
    status = "Pass" if score >= 50 else "Fail"
    return f"{name} scored {score}: {status}"

print(get_result("Sita", 78))
print(get_result("Hari", 42))

# Exercise: Safe division with error handling
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero."

print("Division:", divide_numbers(20, 5))
print("Division:", divide_numbers(20, 0))