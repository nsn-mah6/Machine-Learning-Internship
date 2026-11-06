
students = {
    "Ram": 85,
    "Shyam": 67,
    "Mohan": 22,
    "Salina": 95,
    "Sabita": 78,
    "Prakriti": 88
}

def analyse_students(student_marks):
    if not student_marks:
        print("There are no student in records.")
        return

    average = sum(student_marks.values()) / len(student_marks)
    highest_student = max(student_marks, key=student_marks.get)
    lowest_student = min(student_marks, key=student_marks.get)
    passed = [name for name, mark in student_marks.items() if mark >= 32]
    distinction = {name: mark for name, mark in student_marks.items() if mark > 80}
    sorted_students = sorted(
        student_marks.items(), key=lambda item: item[1], reverse=True
    )

    print(f"Average marks: {average:.2f}")
    print(f"Highest: {highest_student} ({student_marks[highest_student]})")
    print(f"Lowest: {lowest_student} ({student_marks[lowest_student]})")
    print(f"Number passed: {len(passed)}")
    print("Passed students:", passed)
    print("Students scoring distinction:", distinction)
    print("Ranking:")
    for rank, (name, mark) in enumerate(sorted_students, start=1):
        print(f"{rank}. {name}: {mark}")

analyse_students(students)