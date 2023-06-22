from collections import deque

players = deque(input().split(", "))

rows, cols = 6, 6

maze = []
players_hit_wall = []

for r in range(rows):
    line = input().split()
    maze.append(line)

while True:
    position = input()
    player_position = [int(position[1]), int(position[4])]
    current_player = players.popleft()

    if players_hit_wall:
        if current_player == players_hit_wall[0]:
            players.append(current_player)
            players_hit_wall.pop(0)
            continue

    if maze[player_position[0]][player_position[1]] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif maze[player_position[0]][player_position[1]] == "T":
        print(f"{current_player} is out of the game! The winner is {players.popleft()}.")
        break

    elif maze[player_position[0]][player_position[1]] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        is_wall_hit = True
        players_hit_wall.append(current_player)

    players.append(current_player)

# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
#
# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)
#
# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
