def valid_coordinates(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    command, *data = line.split()
    numbers = [int(x) for x in data]

    if valid_coordinates(numbers[0], numbers[1]):

        if command == "Add":
            matrix[numbers[0]][numbers[1]] += numbers[2]
        elif command == "Subtract":
            matrix[numbers[0]][numbers[1]] -= numbers[2]

    else:
        print("Invalid coordinates")

[print(*inner) for inner in matrix]

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
