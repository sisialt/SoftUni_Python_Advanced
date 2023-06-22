def movie_organizer(*args):
    film_genres = {}

    for movie_name, genre in args:
        if genre not in film_genres:
            film_genres[genre] = []
        film_genres[genre].append(movie_name)

    sorted_film_genres = sorted(film_genres.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for genre, movie_name in sorted_film_genres:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()

def make_a_move(row_, col_, matrix):
    found_hazelnuts = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        found_hazelnuts += 1
    matrix[row_][col_] = '*'
    return found_hazelnuts, matrix


rows = int(input())
commands = input().split(", ")
field = []
hazelnuts = 0
die = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1
    result = make_a_move(squirrel_position[0], squirrel_position[1], field)
    if not result:
        die = True
        break
    count_hazelnuts, field = result[0], result[1]
    hazelnuts += count_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")



# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****
#
# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***
#
# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
