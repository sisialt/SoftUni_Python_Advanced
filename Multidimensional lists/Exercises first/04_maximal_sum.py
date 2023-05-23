rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_submatrix = []

for i in range(rows - 2):
    for j in range(cols - 2):
        current_submatrix = [[matrix[row][col] for col in range(j, 3 + j)] for row in range(i, 3 + i)]
        current_sum = sum([sum(inner_list) for inner_list in current_submatrix])

        if max_sum < current_sum:
            max_sum = current_sum
            max_submatrix = current_submatrix

print(f"Sum = {max_sum}")
[print(*inner) for inner in max_submatrix]

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
