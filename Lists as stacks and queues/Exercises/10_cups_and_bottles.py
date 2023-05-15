from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_filled = deque([int(x) for x in input().split()])

wasted_water = 0

while cups_capacity and bottles_filled:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_filled.pop()

    if current_bottle < current_cup:

        # cups_capacity.appendleft(current_cup - current_bottle)

        current_cup -= current_bottle

        while current_cup > 0:
            current_bottle = bottles_filled.pop()
            current_cup -= current_bottle
        wasted_water += abs(current_cup)
    else:
        wasted_water += current_bottle - current_cup

if not cups_capacity:
    print(f"Bottles: ", end='')
    print(*bottles_filled, sep=' ')
else:
    print("Cups: ", end='')
    print(*cups_capacity, sep=' ')

print(f"Wasted litters of water: {wasted_water}.")
