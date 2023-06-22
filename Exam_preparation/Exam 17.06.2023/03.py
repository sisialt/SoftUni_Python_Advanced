def gather_credits(needed_credits, *args):
    gathered_credits = 0
    courses = []

    for arg in args:
        course_name = arg[0]
        course_credits = arg[1]

        if gathered_credits < needed_credits:
            if course_name in courses:
                continue

            courses.append(course_name)
            gathered_credits += course_credits

        else:
            break

    if gathered_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
               f"Courses: {', '.join(sorted(courses))}"

    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
print()