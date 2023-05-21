from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
honey_making_process = deque(input().split())

honey_made = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    elif current_bee < current_nectar:
        current_symbol = honey_making_process.popleft()

        if current_symbol == "+":
            honey_made += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            honey_made += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            honey_made += abs(current_bee * current_nectar)
        elif current_symbol == "/":
            honey_made += abs(current_bee / current_nectar)

print(f"Total honey made: {honey_made}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")

# lines 15-18: forgot to add the bee back if not enough nectar

# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# symbols = deque(input().split())
#
# total_honey = 0
#
# operations = {
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y,
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
# }
#
# while bees and nectar:
#     curr_bee = bees.popleft()
#     curr_nectar = nectar.pop()
#
#     if curr_nectar < curr_bee:
#         bees.appendleft(curr_bee)
#     elif curr_nectar > curr_bee:
#         total_honey += abs(operations[symbols.popleft()](curr_bee, curr_nectar))
#
# print(f"Total honey made: {total_honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
#
# 10 20 30 40
# 11 2 3 4
# + / + +
