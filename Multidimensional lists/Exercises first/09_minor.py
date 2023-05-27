rows = int(input())
moves = input().split()

matrix = []
coals_positions = []
start_position, end_position = tuple(), tuple()
collected_coals = 0

for i in range(rows):
    inner_list = input().split()
    matrix.append(inner_list)
    if "s" in inner_list:
        start_position = (i, inner_list.index("s"))
    if "e" in inner_list:
        end_position = (i, inner_list.index("e"))
    if "c" in inner_list:
        for j in range(len(inner_list)):
            if inner_list[j] == "c":
                coals_positions.append([i, j])

current_position = list(start_position)
total_coals = len(coals_positions)

for move in moves:
    if move == "left":
        if current_position[1] == 0:
            continue
        current_position = [current_position[0], current_position[1] - 1]
    elif move == "right":
        if current_position[1] == rows - 1:
            continue
        current_position = [current_position[0], current_position[1] + 1]
    elif move == "up":
        if current_position[0] == 0:
            continue
        current_position = [current_position[0] - 1, current_position[1]]
    elif move == "down":
        if current_position[0] == rows - 1:
            continue
        current_position = [current_position[0] + 1, current_position[1]]

    if current_position in coals_positions:
        coals_positions.remove(current_position)
        matrix[current_position[0]][current_position[1]] = "*"
        collected_coals += 1

        if collected_coals == total_coals:
            print(f"You collected all coal! ({current_position[0]}, {current_position[1]})")
            break

    elif current_position == list(end_position):
        print(f"Game over! ({current_position[0]}, {current_position[1]})")
        break
else:
    print(f"{total_coals - collected_coals} pieces of coal left. ({current_position[0]}, {current_position[1]})")


# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *
