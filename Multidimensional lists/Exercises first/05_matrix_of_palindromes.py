rows, cols = [int(x) for x in input().split()]

matrix = []
first_letter_ascii = 97

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(first_letter_ascii + row) + chr(first_letter_ascii + row + col) + chr(first_letter_ascii + row))

[print(*inner_list) for inner_list in matrix]

# rows, cols = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")
#
#     print()

# 4 6
