rows = int(input())

matrix = []
bunnie_position = []

for r in range(rows):
    inner = input().split()
    matrix.append(inner)

    if "B" in inner:
        bunnie_position = (r, inner.index("B"))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_sum_eggs = 0
max_direction = ""
needed_positions = []

for direction, position in directions.items():
    current_sum = 0
    current_positions = []
    current_position = bunnie_position

    while True:
        next_row, next_col = current_position[0] + position[0], current_position[1] + position[1]

        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
            current_position = [next_row, next_col]

            if matrix[next_row][next_col].isdigit():
                current_sum += int(matrix[next_row][next_col])
                current_positions.append(current_position)
            else:
                break
        else:
            break

    if current_sum >= max_sum_eggs:
        max_sum_eggs = current_sum
        max_direction = direction
        needed_positions = current_positions

print(max_direction)
print(*needed_positions, sep='\n')
print(max_sum_eggs)

# line 43 it was >


# size = int(input())  # прочитаме размера на матрицата
#
# matrix = []  # създаваме променлива, в която да пазим матрицата
# bunny_pos = []  # създаваме променлива, в която да пазим позицията на заека
# best_path = []  # създаваме променлива, в която да пазим най-добрия път
#
# best_direction = None  # създаваме променлива, в която да пазим най-добрата посока
# max_collected_eggs = 0  # създаваме променлива, в която да пазим максималния брой яйца
#
# directions = {  # създаваме променлива, в която да пазим посоките
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
#     matrix.append(input().split())  # прочитаме ред от конзолата, разделяме по спейс и го добавяме към матрицата
#
#     if 'B' in matrix[row]:  # проверяваме дали заека е на този ред
#         bunny_pos = [row, matrix[row].index('B')]  # ако да, запазваме реда и колоната, на които е заека
#
# for direction, positions in directions.items():  # развъртаме цикъл за всяка посока и нейните позиции
#     row, col = [  # запазваме новата позиция, като събираме текущата позиция с тази от речника
#         bunny_pos[0] + positions[0],
#         bunny_pos[1] + positions[1]
#     ]
#     path = []  # създаваме променлива, в която да пазим текущия път
#     collected_eggs = 0  # създаваме променлива, в която да пазим броя на събраните яйца за текущата посока
#
#     while 0 <= row < size and 0 <= col < size:  # развъртаме цикъл с условие докато позицията на яйцето е валидна
#         if matrix[row][col] == 'X':  # проверяваме дали имаме капан на текущата позиция
#             break  # прекратяваме цикъла
#
#         collected_eggs += int(matrix[row][col])  # събираме яйцата на текущата позиция с текущите яйца
#         path.append([row, col])  # добавяме текущата позиция към текущия път
#
#         row += positions[0]  # събираме текущия ред с реда от посоката, в която се движим
#         col += positions[1]  # събираме текущата колона с колоната от посоката, в която се движим
#
#     if collected_eggs >= max_collected_eggs:  # EDGE: проверяваме дали текущите яйца са повече или равни на максималните
#         max_collected_eggs = collected_eggs  # обновяваме максималния брой яйца
#         best_direction = direction  # обновяваме най-добрата посока
#         best_path = path  # обновяваме най-добрия път
#
# print(best_direction)  # принтираме най-добрата посока
# print(*best_path, sep='\n')  # принтираме най-добрия път
# print(max_collected_eggs)  # принтираме максималния брой яйца

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# both 87/100

# def check_valid_index(row, col):
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         return True
#
#
# def go_in_direction(row, col, step_row=0, step_col=0):
#     sum_eggs = 0
#     positions = []
#     next_step_row, next_step_col = step_row, step_col
#
#     for i in range(rows):
#         next_bunnie_position = [row + next_step_row, col + next_step_col]
#         if check_valid_index(next_bunnie_position[0], next_bunnie_position[1]):
#             if matrix[next_bunnie_position[0]][next_bunnie_position[1]] == "X":
#                 return sum_eggs, positions
#             sum_eggs += int(matrix[next_bunnie_position[0]][next_bunnie_position[1]])
#             positions.append(next_bunnie_position)
#             next_step_row += step_row
#             next_step_col += step_col
#             continue
#         return sum_eggs, positions
#
#
# def check_direction(step_r, step_c):
#     go_dir_sum_eggs, positions = go_in_direction(bunnie_row, bunnie_col, step_row=step_r, step_col=step_c)
#     if go_dir_sum_eggs > max_sum_eggs:
#         return go_dir_sum_eggs, positions
#     return 0, []
#
#
# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
#
# for r in range(rows):
#     for c in range(rows):
#         if matrix[r][c] == "B":
#             bunnie_row, bunnie_col = r, c
#
# max_sum_eggs = 0
# direction = ""
# needed_positions = []
#
# right_sum, right_positions = check_direction(step_r=0, step_c=1)
# if right_sum:
#     direction = "right"
#     max_sum_eggs = right_sum
#     needed_positions = right_positions
#
# up_sum, up_positions = check_direction(step_r=-1, step_c=0)
# if up_sum:
#     direction = "up"
#     max_sum_eggs = up_sum
#     needed_positions = up_positions
#
# left_sum, left_positions = check_direction(step_r=0, step_c=-1)
# if left_sum:
#     direction = "left"
#     max_sum_eggs = left_sum
#     needed_positions = left_positions
#
# down_sum, down_positions = check_direction(step_r=1, step_c=0)
# if down_sum:
#     direction = "down"
#     max_sum_eggs = down_sum
#     needed_positions = down_positions
#
# print(direction)
# print(*needed_positions, sep='\n')
# print(max_sum_eggs)