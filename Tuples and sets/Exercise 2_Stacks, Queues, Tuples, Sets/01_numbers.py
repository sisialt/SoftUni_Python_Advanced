from collections import deque

first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

for _ in range(int(input())):
    line_args = deque(input().split())
    command = line_args.popleft()

    if command == "Add":
        first_or_second = line_args.popleft()
        numbers = list(int(x) for x in line_args)

        if first_or_second == "First":
            for num in numbers:
                first_sequence.add(num)

        elif first_or_second == "Second":
            for num in numbers:
                second_sequence.add(num)

    elif command == "Remove":
        first_or_second = line_args.popleft()
        numbers = list(int(x) for x in line_args)

        if first_or_second == "First":
            for num in numbers:
                if num in first_sequence:
                    first_sequence.remove(num)

        elif first_or_second == "Second":
            for num in numbers:
                if num in second_sequence:
                    second_sequence.remove(num)

    elif command == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()  # Add First 5 6 9 3 => ["Add", "First", 5, 6, 9, 3]
#
#     command = first_command + " " + second_command
#
#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first.discard(int(el)) for el in data]
#     elif command == "Remove Second":
#         [second.discard(int(el)) for el in data]
#     else:
#         print(first.issubset(second) or second.issubset(first))
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")

# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(el) for el in x],
#     "Remove Second": lambda x: [second.discard(el) for el in x],
#     "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first)),
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()  # Add First 5 6 9 3 => ["Add", "First", 5, 6, 9, 3]
#
#     command = first_command + " " + second_command
#
#     functions[command]([int(x) for x in data])
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
