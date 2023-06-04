import os

file_name = "text.txt"
root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, file_name)

with open(file_path) as file:
    file_lines = file.readlines()

for i in range(1, len(file_lines) + 1):
    count_letters = 0
    count_punctuation_marks = 0

    line = file_lines[i - 1].replace("\n", "")

    for ch in line:

        if ch.isalpha():
            count_letters += 1
        elif not ch.isdigit() and not ch.isspace():
            count_punctuation_marks += 1

    with open("output.txt", "a") as output:
        output.write(f"Line {i}: {line} ({count_letters})({count_punctuation_marks})\n")

# from string import punctuation
#
# with open("files/text.txt", "r") as file:
#     text = file.readlines()
#
# output_file = open("files/output.txt", "w")
#
# for i in range(len(text)):
#     letters, marks = 0, 0
#
#     for symbol in text[i]:
#         if symbol.isalpha():
#             letters += 1
#         elif symbol in punctuation:
#             marks += 1
#
#     output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")
#
# output_file.close()
