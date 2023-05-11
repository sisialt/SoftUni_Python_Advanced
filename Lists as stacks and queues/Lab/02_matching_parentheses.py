string = input()
open_brackets_as_stack = []

for index in range(len(string)):
    if string[index] == "(":
        open_brackets_as_stack.append(index)
    elif string[index] == ")":
        start_position = open_brackets_as_stack.pop()
        end_position = index
        print(string[start_position:end_position + 1])
        