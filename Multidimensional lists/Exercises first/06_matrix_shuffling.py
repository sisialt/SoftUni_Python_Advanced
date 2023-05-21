rows, cols = [int(x) for x in input().split()]

matrix = []
is_invalid = False

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    if is_invalid:
        print("Invalid input!")
        is_invalid = False

    command = input()

    if command == "END":
        break

    command, *data = command.split()

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


# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
