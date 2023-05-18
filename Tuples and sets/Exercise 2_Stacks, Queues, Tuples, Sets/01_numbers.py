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
