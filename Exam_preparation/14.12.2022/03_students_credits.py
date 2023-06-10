def students_credits(*args):
    courses = {}
    result = []

    for arg in args:
        course_name, *data = arg.split("-")
        course_credits, max_test_points, diyans_points = [int(x) for x in data]

        diyans_credits = (diyans_points / max_test_points) * course_credits

        courses[course_name] = diyans_credits

    total_diyans_credits = sum(courses.values())
    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])

    if total_diyans_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_diyans_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - total_diyans_credits):.1f} credits more for a diploma.")

    [result.append(f"{course[0]} - {course[1]:.1f}") for course in sorted_courses]

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
print()