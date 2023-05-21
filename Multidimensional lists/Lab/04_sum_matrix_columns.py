rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

for j in range(cols):
    current_sum_col = 0
    for i in range(rows):
        current_el = matrix[i][j]
        current_sum_col += current_el
    print(current_sum_col)

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1
