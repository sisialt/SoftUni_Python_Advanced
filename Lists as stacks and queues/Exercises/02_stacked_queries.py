n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    if query[0] == "1":
        number_to_push = int(query[1])
        stack.append(number_to_push)
    elif query[0] == "2":
        if stack:
            stack.pop()
    elif query[0] == "3":
        if stack:
            print(max(stack))
    elif query[0] == "4":
        if stack:
            print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=', ')

print(stack.pop())


# forgot line 12,15,18


# solution lambda
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),  # x == number_data => [1, 97]
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]  # [1, 97]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
#
# print(*numbers, sep=", ")



# numbers = deque()
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]  # [1, 97]
#     command = number_data[0]
#
#     if command == 1:
#         numbers.append(number_data[1])
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
#
# numbers.reverse()
#
# print(*numbers, sep=", ")

