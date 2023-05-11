string = input()
string_as_stack = list(string)

while len(string_as_stack) > 0:
    print(string_as_stack.pop(), end='')
