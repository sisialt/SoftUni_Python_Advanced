import os

file_name = "my_first_file.txt"
root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, file_name)

with open(file_path, "w") as file:
    file.write("I just created my first file!")

