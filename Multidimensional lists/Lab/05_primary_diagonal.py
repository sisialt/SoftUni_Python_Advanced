rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

sum_primary_diagonal = 0

for i in range(rows):
    current_el = matrix[i][i]
    sum_primary_diagonal += current_el

print(sum_primary_diagonal)

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
