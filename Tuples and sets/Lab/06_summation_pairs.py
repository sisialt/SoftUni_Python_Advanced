from collections import deque

unique_integers = deque([int(x) for x in input().split()])
target = int(input())

while unique_integers:
    num1 = unique_integers.popleft()
    for num2 in unique_integers:
        if num2 + num1 == target:
            unique_integers.remove(num2)
            print(f"{num1} + {num2} = {target}")
            break
