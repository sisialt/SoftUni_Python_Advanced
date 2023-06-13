from collections import deque


def check_enough_fireworks():
    for f, c in fireworks.items():
        if c >= 3:
            continue
        return False
    return True


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_powers = deque([int(x) for x in input().split(", ")])

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while firework_effects and explosive_powers:
    current_firework_effect = firework_effects.popleft()

    if current_firework_effect <= 0:
        continue

    current_explosive_power = explosive_powers.pop()

    if current_explosive_power <= 0:
        firework_effects.appendleft(current_firework_effect)
        continue

    sum_effect_power = current_explosive_power + current_firework_effect

    if sum_effect_power % 3 == 0 and sum_effect_power % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        if check_enough_fireworks():
            print("Congrats! You made the perfect firework show!")
            break

    elif sum_effect_power % 3 != 0 and sum_effect_power % 5 == 0:
        fireworks["Willow Fireworks"] += 1
        if check_enough_fireworks():
            print("Congrats! You made the perfect firework show!")
            break

    elif sum_effect_power % 15 == 0:
        fireworks["Crossette Fireworks"] += 1
        if check_enough_fireworks():
            print("Congrats! You made the perfect firework show!")
            break

    else:
        current_firework_effect -= 1
        firework_effects.append(current_firework_effect)
        explosive_powers.append(current_explosive_power)

else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

for f, c in fireworks.items():
    print(f"{f}: {c}")

#
# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
#
# -15, -8, 0, -16, 0, -22
# 10, 5
