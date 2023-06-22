rows, cols = 6, 6

board = []
buckets = []
scores = 0

for r in range(rows):
    line = input().split()
    board.append(line)

for _ in range(3):
    throw = input().strip("()").split(", ")
    position = [int(throw[0]), int(throw[1])]

    if 0 <= position[0] < rows and 0 <= position[1] < cols:

        if board[position[0]][position[1]] == "B":
            if [position[0], position[1]] not in buckets:
                buckets.append([position[0], position[1]])

                for i in range(rows):

                    if board[i][position[1]].isdigit():
                        scores += int(board[i][position[1]])

if scores < 100:
    print(f"Sorry! You need {100 - scores} points more to win a prize.")
elif 100 <= scores <= 199:
    prize = "Football"
    print(f"Good job! You scored {scores} points, and you've won {prize}.")
elif 200 <= scores <= 299:
    prize = "Teddy Bear"
    print(f"Good job! You scored {scores} points, and you've won {prize}.")
elif 300 <= scores:
    prize = "Lego Construction Set"
    print(f"Good job! You scored {scores} points, and you've won {prize}.")


# 10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)
#
# B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)
