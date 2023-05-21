rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()

position = ()

for i in range(rows):
    if position:
        break

    for j in range(rows):
        current_el = matrix[i][j]

        if current_el == searched_symbol:
            position = (i, j)
            break

print(position) if position else print(f"{searched_symbol} does not occur in the matrix")
