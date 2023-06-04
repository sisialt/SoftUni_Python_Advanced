import os

file_name = "text.txt"
root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, file_name)

with open(file_path) as file:
    file_lines = file.readlines()

for i in range(0, len(file_lines), 2):
    line = file_lines[i].replace("\n", "")

    for ch in line:
        if ch in ["-", ",", ".", "!", "?"]:
            line = line.replace(ch, "@")

    words = line.split()
    words.reverse()

    print(*words)


# symbols = ["-", ",", ".", "!", "?"]
#
# with open("files/text.txt", "r") as file:
#     text = file.readlines()
#
# for row in range(0, len(text), 2):
#
#     for symbol in symbols:
#         text[row] = text[row].replace(symbol, "@")
#
#     print(*text[row].split()[::-1], sep=" ")
