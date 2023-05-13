from collections import deque

parentheses = deque(input())
opening_parentheses = deque()
opening = ["(", "{", "["]

while parentheses:
    current_parenthesis = parentheses.popleft()
    if current_parenthesis in opening:
        opening_parentheses.append(current_parenthesis)
    elif not opening_parentheses:
        print("NO")
        break
    else:
        if f"{opening_parentheses.pop() + current_parenthesis}" not in "()[]{}":
            print("NO")
            break
else:
    if not opening_parentheses:
        print("YES")
    else:
        print("NO")


# while parentheses:
#     current_parenthesis = parentheses.popleft()
#     if current_parenthesis in opening:
#         opening_parentheses.append(current_parenthesis)
#     elif not opening_parentheses:
#         print("NO")
#         break
#     else:
#         last_opening_parenthesis = opening_parentheses.pop()
#         if last_opening_parenthesis == "[":
#             current_closing_parenthesis_should_be = "]"
#         elif last_opening_parenthesis == "{":
#             current_closing_parenthesis_should_be = "}"
#         elif last_opening_parenthesis == "(":
#             current_closing_parenthesis_should_be = ")"
#         else:
#             current_closing_parenthesis_should_be = ""
#
#         if current_closing_parenthesis_should_be != current_parenthesis:
#             print("NO")
#             break
