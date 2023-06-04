import os

file_name = "numbers.txt"
root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, file_name)

try:
    with open(file_path, "r") as file:
        numbers = [int(el) for el in file.read().split("\n") if el]
        print(sum(numbers))

except FileNotFoundError:
    print("File not found")
