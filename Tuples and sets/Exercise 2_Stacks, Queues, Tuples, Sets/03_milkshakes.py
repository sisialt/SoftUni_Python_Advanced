from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_milk = deque([int(x) for x in input().split(", ")])

count_milkshakes = 0
five_milkshakes_done = False

while count_milkshakes != 5 and chocolates and cups_milk:

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

    else:
        current_chocolate -= 5

        chocolates.append(current_chocolate)
        cups_milk.append(current_cup)

if count_milkshakes == 5:
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

# from collections import deque
#
# chocolates = deque(int(x) for x in input().split(", "))
# cups_of_milk = deque(int(x) for x in input().split(", "))
#
# milkshakes = 0
#
# while milkshakes != 5 and chocolates and cups_of_milk:
#     chocolate = chocolates.pop()
#     cup_of_milk = cups_of_milk.popleft()
#
#     if chocolate <= 0 and cup_of_milk <= 0:
#         continue
#     elif chocolate <= 0:
#         cups_of_milk.appendleft(cup_of_milk)
#         continue
#     elif cup_of_milk <= 0:
#         chocolates.append(chocolate)
#         continue
#
#     if chocolate == cup_of_milk:
#         milkshakes += 1
#     else:
#         cups_of_milk.append(cup_of_milk)
#         chocolates.append(chocolate - 5)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
# print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
