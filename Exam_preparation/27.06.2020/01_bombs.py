from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])

bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

created_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

is_filled = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    for bomb in bombs:
        if current_casing + current_effect == bombs[bomb]:
            created_bombs[bomb] += 1
            break
    else:
        current_casing -= 5
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing)

    for bomb in created_bombs:
        if created_bombs[bomb] < 3:
            break
    else:
        print(f"Bene! You have successfully filled the bomb pouch!")
        is_filled = True
        break

if not is_filled:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for b in sorted(created_bombs):
    print(f"{b}: {created_bombs[b]}")

# 5, 25, 25, 115
# 5, 15, 25, 35
#
# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10
