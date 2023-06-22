from collections import deque


def is_duck(t):
    for duck, values in rubber_ducks.items():
        if t in range(values[0], values[1] + 1):
            ducks_given[duck] += 1
            return True
    return False


programmers_time = deque([int(x) for x in input().split()])
tasks_count = deque([int(x) for x in input().split()])

rubber_ducks = {
    "Darth Vader Ducky": (0, 60),
    "Thor Ducky": (61, 120),
    "Big Blue Rubber Ducky": (121, 180),
    "Small Yellow Rubber Ducky": (181, 240)
}

ducks_given = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmers_time and tasks_count:
    current_time = programmers_time.popleft()
    current_task = tasks_count.pop()

    calculated_time = current_task * current_time

    if not is_duck(calculated_time):
        current_task -= 2
        tasks_count.append(current_task)
        programmers_time.append(current_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks_given.items():
    print(f"{duck}: {count}")


# 10 15 12 18 22 6
# 12 16 5 6 9 1
#
# 2 55 17 31 23
# 7 5 17 4 27
