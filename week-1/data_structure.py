# Exercise: List operations
marks = [78, 85, 90, 66, 72]
marks.append(88)
marks[1] = 87
print("Marks:", marks)
print("First mark:", marks[0])
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))

# Exercise: Tuple
coordinates = (27.7172, 85.3240)
print("\nCoordinates:", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Exercise: Set removes duplicates
departments = ["IT", "Data", "IT", "AI", "Data", "Networking"]
unique_departments = set(departments)
print("\nUnique departments:", unique_departments)

# Exercise: Dictionary
student = {"name": "Ram", "age": 22, "marks": 85}
student["course"] = "Data Science"
student["marks"] = 90
print("\nStudent:", student)
for key, value in student.items():
    print(f"{key}: {value}")