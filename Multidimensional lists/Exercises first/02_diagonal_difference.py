rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for i in range(rows):
    sum_primary_diagonal += matrix[i][i]
    sum_secondary_diagonal += matrix[i][rows - i - 1]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))


# 3
# 11 2 4
# 4 5 6
# 10 8 -12
