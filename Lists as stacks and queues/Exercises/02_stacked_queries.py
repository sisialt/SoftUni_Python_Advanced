n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    if query[0] == "1":
        number_to_push = int(query[1])
        stack.append(number_to_push)
    elif query[0] == "2":
        if not stack:
            continue
        stack.pop()
    elif query[0] == "3":
        if not stack:
            continue
        print(max(stack))
    elif query[0] == "4":
        if not stack:
            continue
        print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=', ')

print(stack.pop())


# forgot line 12,13/16,17/20,21
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4

