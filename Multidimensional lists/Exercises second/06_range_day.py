matrix = []
shot_targets = []
targets = []
start_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(5):
    inner = input().split()
    matrix.append(inner)

    if "A" in inner:
        start_position = (r, inner.index("A"))

    if "x" in inner:

        for ch in inner:

            if ch == "x":
                targets.append([r, inner.index(ch)])

for _ in range(int(input())):
    line_args = input().split()

    command = line_args[0]
    direction = line_args[1]

    if command == "move":
        steps = int(line_args[2])

        steps_dict = {
            "up": (-steps, 0),
            "down": (steps, 0),
            "left": (0, -steps),
            "right": (0, steps)
        }

        next_row, next_col = start_position[0] + steps_dict[direction][0], start_position[1] + steps_dict[direction][1]

        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):

            if matrix[next_row][next_col] == ".":
                start_position = (next_row, next_col)

    elif command == "shoot":
        current_position_to_be_shot = list(start_position)

        while True:
            shoot_row = current_position_to_be_shot[0] + directions[direction][0]
            shoot_col = current_position_to_be_shot[1] + directions[direction][1]

            if 0 <= shoot_row < len(matrix) and 0 <= shoot_col < len(matrix):

                if matrix[shoot_row][shoot_col] == "x":
                    shot_targets.append([shoot_row, shoot_col])
                    matrix[shoot_row][shoot_col] = "."
                    break

                current_position_to_be_shot = [shoot_row, shoot_col]

            else:
                break

if len(shot_targets) == len(targets):
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {len(targets) - len(shot_targets)} targets left.")

print(*shot_targets, sep='\n')


# 90/100 gyrmi


# def move(direction, steps):  # създаваме фунцкия move, първи параметър посоката и втори стъпките int
#     r = my_position[0] + (directions[direction][0] * steps)  # намираме реда и колоната като умножаваме стойностите от
#     c = my_position[1] + (directions[direction][1] * steps)  # посоката по стъпките и събираме с текущите координати
#
#     if not (0 <= r < SIZE and 0 <= c < SIZE):  # проверяваме дали позицията, на която искаме да стъпим е валидна
#         return my_position  # ако не е, връщаме текущата позиция
#     if field[r][c] == 'x':  # проверяваме дали на позицията, на която искаме да стъпим има мишена
#         return my_position  # ако да, връщаме текущата позиция
#
#     return [r, c]  # връщаме новата позиция
#
#
# def shoot(direction):  # създаваме фунцкия shoot, параметър посоката на стрелба
#     r = my_position[0] + directions[direction][0]  # намираме реда и колоната като събираме координатите от посоката
#     c = my_position[1] + directions[direction][1]  # с тези, на които се намираме
#
#     while 0 <= r < SIZE and 0 <= c < SIZE:  # развъртаме цикъл докато координатите са валидни
#         if field[r][c] == 'x':  # проверяваме дали куршума е достигнал мишена
#             field[r][c] = '.'  # ако да, заменяме х с точка
#             return [r, c]  # връщаме позицията на улучената мишена
#
#         r += directions[direction][0]  # събираме координатите от посоката
#         c += directions[direction][1]  # с тези, на които се намира куршума
#
#
# SIZE = 5  # запазваме размера на матрицата в променлива
# field = []  # създаваме променлива, в която да пазим матрицата
#
# targets = 0  # създаваме променлива, в която да пазим броя на мишените в полето
# targets_hit = 0  # създаваме променлива, в която да пазим броя на уцелените мишени
# targets_hit_positions = []  # създаваме променлива, в която да пазим координатите на уцелените мишени
#
# my_position = []  # създаваме променлива, в която да пазим позицията ни
#
# directions = {  # създаваме променлива, в която да пазим посоките
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# for row in range(SIZE):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
#     field.append(input().split())  # прочитаме ред от конзолата, разделяме го по спейс и го добавяме към матрицата
#
#     if 'A' in field[row]:  # проверяваме дали нашата позиция се намира на този ред
#         my_position = [row, field[row].index('A')]  # запазваме нашата позиция
#
#     targets += field[row].count('x')  # увеличаваме броя на мишените с броя им на реда
#
# for _ in range(int(input())):  # развъртаме цикъл за очаквания брой команди
#     command_info = input().split()  # прочитаме командата и я разделяме по спейс
#
#     if command_info[0] == 'move':  # проверяваме дали командата е move
#         my_position = move(command_info[1], int(command_info[2]))  # извикваме функцията move, стъпките стават int
#     elif command_info[0] == 'shoot':  # проверяваме дали командата е shoot
#         target_down_pos = shoot(command_info[1])  # извикваме функцията shoot, параметър е посоката
#
#         if target_down_pos:  # проверяваме дали сме свалили мишена
#             targets_hit_positions.append(target_down_pos)  # добавяме позицията на свалената мишена
#             targets_hit += 1  # увеличаваме броя на свалените мишени с 1
#
#         if targets_hit == targets:  # проверяваме дали всички мишени са свалени
#             print(f'Training completed! All {targets} targets hit.')  # принтираме, че успешно сме завършили обучението
#             break  # прекратяваме цикъла
#
# if targets_hit < targets:  # проверяваме дали са останали мишени
#     print(f'Training not completed! {targets - targets_hit} targets left.')  # принтираме неуспешно завършено обучение
#
# print(*targets_hit_positions, sep="\n")  # принтираме позициите на свалените мишени

# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right


# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left
