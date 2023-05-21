from collections import deque
from functools import reduce

expression = deque(input().split())

numbers = deque()

while expression:
    el = expression.popleft()

    if el.isdigit() or (el[0] == "-" and el[1:].isdigit()):
        numbers.append(int(el))
        continue

    result = numbers.popleft()

    while numbers:
        num = numbers.popleft()

        if el == "*":
            result *= num
        elif el == "/":
            result //= num
        elif el == "-":
            result -= num
        elif el == "+":
            result += num

    numbers.appendleft(result)

print(result)


# from functools import reduce
# from math import floor
#
# expression = input().split()  # 6 3 - 2 1 * 5 /
#
# idx = 0
#
# functions = {
#     "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
# }
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element in "*/+-":
#         expression[0] = functions[element](idx)
#         [expression.pop(1) for i in range(idx)]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))

# from collections import deque
# from math import floor
#
# expression = deque(input().split())  # 6 3 5 - 2 1 * 5 /
#
# idx = 0
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element == "*":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#     elif element == "/":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == "+":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#     elif element == "-":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in "*/+-":
#         del expression[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))

# def calculate(sign, result, num):
#     if sign == "*":
#         result *= num
#     elif sign == "/":
#         result //= num
#     elif sign == "-":
#         result -= num
#     elif sign == "+":
#         result += num
#
#     return result
#
#
# expression = deque(input().split())
#
# numbers = deque()
#
# while expression:
#     el = expression.popleft()
#
#     if el.isdigit() or (el[0] == "-" and el[1:].isdigit()):
#         numbers.append(int(el))
#         continue
#
#     if el == "*":
#         print(*numbers, sep=' * ', end='')
#
#         result = numbers.popleft()
#
#         while numbers:
#             num = numbers.popleft()
#             result *= num
#
#     elif el == "/":
#
#         print(*numbers, sep=' / ', end='')
#
#         result = numbers.popleft()
#
#         while numbers:
#             num = numbers.popleft()
#             result //= num
#
#     elif el == "+":
#
#         print(*numbers, sep=' + ', end='')
#
#         result = numbers.popleft()
#
#         while numbers:
#             num = numbers.popleft()
#             result += num
#
#     elif el == "-":
#         print(*numbers, sep=' - ', end='')
#
#         result = numbers.popleft()
#
#         while numbers:
#             num = numbers.popleft()
#             result -= num
#
#     print(f" = {result}")
#
#     numbers.appendleft(result)

