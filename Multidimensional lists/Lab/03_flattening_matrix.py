rows = int(input())

matrix = []
flattened_matrix = []

for i in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)
    flattened_matrix.extend(inner_list)

print(flattened_matrix)

# 2
# 1, 2, 3
# 4, 5, 6
