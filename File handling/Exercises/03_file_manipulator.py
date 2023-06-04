import os

root_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    line = input()

    if line == "End":
        break

    command, file_name, *data = line.split("-")

    file_path = os.path.join(root_dir, file_name)

    if command == "Create":
        with open(file_path, "w") as file:
            pass

    elif command == "Add":
        content = data[0]

        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string = data[0]
        new_string = data[1]

        try:
            with open(file_path, "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":

        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")

# import os
#
#
# while True:
#     command, *info = input().split("-")  # Replace-example.txt-_-=
#
#     if command == "Create":
#         with open(f"files/{info[0]}", "w"): pass
#
#     elif command == "Add":
#         with open(f"files/{info[0]}", "a") as file:
#             file.write(f"{info[1]}\n")
#
#     elif command == "Replace":
#         try:
#             with open(f"files/{info[0]}", "r+") as file:
#                 text = file.read()
#                 text = text.replace(info[1], info[2])
#
#                 file.seek(0)
#                 file.write(text)
#
#         except FileNotFoundError:
#             print(f"An error occurred")
#
#     elif command == "Delete":
#         try:
#             os.remove(f"files/{info[0]}")
#         except FileNotFoundError:
#             print(f"An error occurred")
#
#     elif command == "End":
#         break
