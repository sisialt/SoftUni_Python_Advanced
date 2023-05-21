rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for i in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    sum_matrix += sum(inner_list)
    matrix.append(inner_list)

print(sum_matrix)
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0