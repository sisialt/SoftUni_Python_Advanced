rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

count = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        el_below = matrix[i + 1][j]
        diagonal_element = matrix[i + 1][j + 1]

        if current_el == next_el == el_below == diagonal_element:
            count += 1

print(count)




# 3 4
# A B B D
# E B B B
# I J B B
