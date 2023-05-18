from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_milk = deque([int(x) for x in input().split(", ")])

count_milkshakes = 0
five_milkshakes_done = False

while chocolates and cups_milk:

    current_chocolate = chocolates.pop()
    current_cup = cups_milk.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue
    elif current_chocolate <= 0:
        cups_milk.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        count_milkshakes += 1

        if count_milkshakes == 5:
            five_milkshakes_done = True
            break

    else:
        current_chocolate -= 5

        if current_chocolate > 0:
            chocolates.append(current_chocolate)

        cups_milk.append(current_cup)

if five_milkshakes_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: ", end='')
    print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: ", end='')
    print(*cups_milk, sep=', ')
else:
    print("Milk: empty")

# lines 14-21: logic combinations was false
