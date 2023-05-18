from collections import deque

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

