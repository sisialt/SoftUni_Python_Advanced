def get_magic_triangle(n):
    matrix = [[1], [1, 1]]

    for i in range(n - 2):
        next_line = [matrix[-1][0]]

        for j in range(i + 1):
            next_line.append(matrix[-1][j] + matrix[-1][j + 1])

        next_line.append(matrix[-1][-1])
        matrix.append(next_line)

    return matrix


print(get_magic_triangle(5))