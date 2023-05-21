from collections import deque

rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

coordinates_bombs = deque(input().split())

sum_alive_cells = 0
count_alive = 0

while coordinates_bombs:
    current_bomb = coordinates_bombs.popleft().split(',')
    current_bomb_row, current_bomb_col = int(current_bomb[0]), int(current_bomb[1])

    current_element = matrix[current_bomb_row][current_bomb_col]

    for row in range(current_bomb_row - 1, current_bomb_row + 2):
        for col in range(current_bomb_col - 1, current_bomb_col + 2):
            if not 0 <= row < rows or not 0 <= col < rows:
                continue

            if matrix[row][col] <= 0:
                continue

            matrix[row][col] -= current_element

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] > 0:
            sum_alive_cells += matrix[row][col]
            count_alive += 1

print(f"Alive cells: {count_alive}\nSum: {sum_alive_cells}")
[print(*inner_list) for inner_list in matrix]

# 90/100 judge

# Solution 80/100 judge

# sum_alive_cells = sum([sum(inner_list) for inner_list in matrix])
# count_alive = rows * rows
#
# // - //
#
#             if matrix[row][col] - current_element > 0:
#                 sum_alive_cells -= current_element
#             else:
#                 sum_alive_cells -= matrix[row][col]
#
#             matrix[row][col] -= current_element
#
#             if matrix[row][col] <= 0:
#                 count_alive -= 1
# // - //

# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
