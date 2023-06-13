size = int(input())

field = []
player_position = []
players_path = []
collected_coins = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(size):
    line = input().split()
    field.append(line)

    if "P" in line:
        player_position = [r, line.index("P")]
        players_path.append(player_position)

while collected_coins < 100:
    command = input()

    if command not in directions:
        continue

    next_row = player_position[0] + directions[command][0]
    next_col = player_position[1] + directions[command][1]

    if not (0 <= next_row < size and 0 <= next_col < size):
        if command == "up":
            next_row = size - 1
        elif command == "down":
            next_row = 0
        elif command == "left":
            next_col = size - 1
        elif command == "right":
            next_col = 0

    player_position = [next_row, next_col]
    players_path.append(player_position)

    if field[next_row][next_col].isdigit():
        collected_coins += int(field[next_row][next_col])
        field[next_row][next_col] = "."

    elif field[next_row][next_col] == "X":
        collected_coins //= 2
        print(f"Game over! You've collected {collected_coins} coins.")
        break

else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
print(*players_path, sep="\n")

# 5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# left
# right
# right
# up
# up
# right
#
# 8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# down
# up
# left
