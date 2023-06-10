from collections import deque


def is_valid_index(ind):
    if 0 <= ind < len(matrix):
        return True
    return False


def is_pawn_on_diagonal(col):
    if is_valid_index(col):
        diagonal = matrix[next_row][col]

        if diagonal != "-":
            return True

    return False


ROWS, COLUMNS = 8, 8

matrix = []
white_pawn_position, black_pawn_position = [], []

players = deque(["White", "Black"])

for r in range(ROWS):
    line = input().split()
    matrix.append(line)

    if "w" in line:
        white_pawn_position = [r, line.index("w")]
    elif "b" in line:
        black_pawn_position = [r, line.index("b")]

while True:
    current_player = players.popleft()

    if current_player == "White":
        next_row = white_pawn_position[0] - 1
        current_position = white_pawn_position.copy()
    else:
        next_row = black_pawn_position[0] + 1
        current_position = black_pawn_position.copy()

    if is_pawn_on_diagonal(current_position[1] - 1):
        current_position = [next_row, current_position[1] - 1]
        print(f"Game over! {current_player} win, capture on {chr(current_position[1] + 97) + str(8 - current_position[0])}.")
        break

    if is_pawn_on_diagonal(current_position[1] + 1):
        current_position = [next_row, current_position[1] + 1]
        print(f"Game over! {current_player} win, capture on {chr(current_position[1] + 97) + str(8 - current_position[0])}.")
        break

    if is_valid_index(next_row):
        matrix[current_position[0]][current_position[1]] = "-"

        if current_player == "White":
            matrix[next_row][current_position[1]] = "w"
            white_pawn_position = [next_row, current_position[1]]
            if next_row == 0:
                print(f"Game over! {current_player} pawn is promoted to a queen at {chr(current_position[1] + 97) + str(ROWS - next_row)}.")
                break
        else:
            matrix[next_row][current_position[1]] = "b"
            black_pawn_position = [next_row, current_position[1]]
            if next_row == ROWS - 1:
                print(f"Game over! {current_player} pawn is promoted to a queen at {chr(current_position[1] + 97) + str(ROWS - next_row)}.")
                break

    players.append(current_player)

# SIZE = 8
#
# board = []
# positions = [[], []]
#
#
# def save_positions(search_for, index_to_save, r):
#     if search_for in board[r]:
#         positions[index_to_save].append(r)
#         positions[index_to_save].append(board[r].index(search_for))
#
#
# for row in range(SIZE):
#     board.append(input().split())  # - - - - - b - => [-, -, -, -, -, b, -]
#
#     save_positions("w", 0, row)
#     save_positions("b", 1, row)
#
# if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
#     if SIZE - positions[0][0] - 1 <= positions[1][0]:
#         print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
#     else:
#         print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
# else:
#     place = (positions[0][0] + positions[1][0]) // 2
#
#     if positions[0][0] % 2 == positions[1][0] % 2:
#         print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
#     else:
#         print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")

# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - b - - - - - -
# - - - - - - - -
# w - - - - - - -
# - - - - - - - -
# - - - - - - - -
#print(white_pawn_position, black_pawn_position)

