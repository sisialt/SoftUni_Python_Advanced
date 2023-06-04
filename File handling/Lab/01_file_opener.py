import os

file_name = "text.txt"
root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, file_name)

if os.path.isfile(file_path):
    print("File found")
else:
    print("File not found")
