from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches_count = 0

while females and males:
    current_female = females.popleft()

    if current_female <= 0:
        continue
    elif current_female % 25 == 0:
        females.popleft()
        continue

    current_male = males.pop()

    if current_male <= 0:
        females.appendleft(current_female)
        continue
    elif current_male % 25 == 0:
        females.appendleft(current_female)
        males.pop()
        continue

    if current_female == current_male:
        matches_count += 1
    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches_count}")

if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")




# 4 5 7 3 6 9 12
# 12 9 6 1
#
# 3 0 3 6 9 0 12
# 12 9 6 1 2 3 15 13 4
