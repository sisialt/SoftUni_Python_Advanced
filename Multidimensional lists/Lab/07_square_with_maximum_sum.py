rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

max_sum = float("-inf")
sum_elements_submatrix = 0
submatrix = []

for i in range(rows - 1):
    for j in range(cols - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        el_below = matrix[i + 1][j]
        diagonal_element = matrix[i + 1][j + 1]

        sum_elements_submatrix = current_el + next_el + el_below + diagonal_element

        if max_sum < sum_elements_submatrix:
            max_sum = sum_elements_submatrix
            submatrix = [[current_el, next_el], [el_below, diagonal_element]]

[print(*inner_list) for inner_list in submatrix]
print(max_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
