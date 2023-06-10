from collections import deque

MAX_CAFFEINE = 300

caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

stamats_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    caffeine_in_drink = current_caffeine * current_energy_drink

    if caffeine_in_drink + stamats_caffeine <= MAX_CAFFEINE:
        stamats_caffeine += caffeine_in_drink
    else:
        energy_drinks.append(current_energy_drink)
        stamats_caffeine -= 30
        if stamats_caffeine < 0:
            stamats_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")

# line 16 must be also equal

# 34, 2, 3
# 40, 100, 250
#
# 1, 16, 8, 14, 5
# 27, 23
#
# 1, 23, 2, 1, 42, 22, 7, 14
# 51, 100, 3, 7
