from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
honey_making_process = deque(input().split())

honey_made = 0
no_nectar = False

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    while current_nectar < current_bee:
        if not nectar:
            no_nectar = True
            bees.appendleft(current_bee)
            break

        current_nectar = nectar.pop()

    if not no_nectar:
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

if nectar or bees:

    if bees:
        print(f"Bees left: {', '.join([str(x) for x in bees])}")
    else:
        print(f"Nectar left: {', '.join([str(x) for x in nectar])}")

# lines 15-18: forgot to add the bee back if not enough nectar

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
#
# 10 20 30 40
# 11 2 3 4
# + / + +
