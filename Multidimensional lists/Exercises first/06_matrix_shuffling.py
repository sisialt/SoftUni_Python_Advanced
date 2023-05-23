rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

is_invalid = False

while True:
    if is_invalid:
        print("Invalid input!")
        is_invalid = False

    command, *data = input().split()

    if command == "END":
        break

    if command != "swap" or len(data) != 4:
        is_invalid = True
        continue

    coordinates = []

    for i in range(len(data)):
        ch = data[i]

        if not ch.isdigit():
            is_invalid = True
            break

        if i % 2 == 0:
            if not 0 <= int(ch) < len(matrix):
                is_invalid = True
                break
        else:
            if not 0 <= int(ch) < len(matrix[0]):
                is_invalid = True
                break

        coordinates.append(int(ch))

    if is_invalid:
        continue

    row1, col1, row2, col2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    [print(*inner_list) for inner_list in matrix]


# def check_valid_indices(indices):
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)
#
#
# def swap_command(command, indices):
#     if check_valid_indices(indices) and command == "swap" and len(indices) == 4:
#         row1, col1, row2, col2 = indices
#
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#         print(*[' '.join(r) for r in matrix], sep="\n")
#     else:
#         print("Invalid input!")
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)
# valid_cols = range(cols)
#
# while True:
#     command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]
#
#     if command_type == "END":
#         break
#
#     swap_command(command_type, info)


# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
