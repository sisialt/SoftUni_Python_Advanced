from collections import deque


def is_winner():
    if scores[current_player][0] <= 0:
        return True
    return False


ROWS, COLUMNS = 7, 7
START_SCORE = 501

dartboard = []

players = deque(input().split(", "))

scores = {players[0]: [START_SCORE, 0], players[1]: [START_SCORE, 0]}

for r in range(ROWS):
    line = input().split()
    dartboard.append(line)

while True:
    hit = input().strip("()").split(", ")
    hit_position = [int(hit[0]), int(hit[1])]

    current_player = players.popleft()
    scores[current_player][1] += 1

    if 0 <= hit_position[0] < ROWS and 0 <= hit_position[1] < COLUMNS:
        current_field = dartboard[hit_position[0]][hit_position[1]]

        if current_field.isdigit():
            scores[current_player][0] -= int(current_field)

            if is_winner():
                print(f"{current_player} won the game with {scores[current_player][1]} throws!")
                break

        elif current_field == "D":
            doubled_sum_scores = 2 * (int(dartboard[hit_position[0]][0]) + int(dartboard[hit_position[0]][-1])
                                      + int(dartboard[0][hit_position[1]]) + int(dartboard[-1][hit_position[1]]))
            scores[current_player][0] -= doubled_sum_scores

            if is_winner():
                print(f"{current_player} won the game with {scores[current_player][1]} throws!")
                break

        elif current_field == "T":
            tripled_sum_scores = 3 * (int(dartboard[hit_position[0]][0]) + int(dartboard[hit_position[0]][-1])
                                      + int(dartboard[0][hit_position[1]]) + int(dartboard[-1][hit_position[1]]))
            scores[current_player][0] -= tripled_sum_scores

            if is_winner():
                print(f"{current_player} won the game with {scores[current_player][1]} throws!")
                break

        elif current_field == "B":
            print(f"{current_player} won the game with {scores[current_player][1]} throws!")
            break

    players.append(current_player)

# function returned print(), which was not considered True


# Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)
#
# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)
