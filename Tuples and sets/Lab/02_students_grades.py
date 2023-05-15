students = {}

for _ in range(int(input())):
    student, grade = input().split()
    grade = float(grade)

    if student not in students:
        students[student] = []
    students[student].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join(str(f'{gr:.2f}') for gr in grades)} (avg: {average_grade:.2f})")
