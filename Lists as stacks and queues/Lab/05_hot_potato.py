from collections import deque

kids = deque(input().split())
number = int(input())

while len(kids) != 1:
    kids.rotate(-(number - 1))
    kid_to_remove = kids.popleft()
    print(f"Removed {kid_to_remove}")

print(f"Last is {kids.popleft()}")
kids.a