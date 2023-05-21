from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(input())

rest_snake = snake.copy()
matrix = []

for row in range(rows):
    matrix.append([])

    if row % 2 == 0:

        for col in range(cols):
            if not rest_snake:
                rest_snake = snake.copy()
            current = rest_snake.popleft()
            matrix[row].append(current)

    else:

        for col in range(cols):
            if not rest_snake:
                rest_snake = snake.copy()
            current = rest_snake.popleft()
            matrix[row].insert(0, current)

[print(''.join(inner)) for inner in matrix]
