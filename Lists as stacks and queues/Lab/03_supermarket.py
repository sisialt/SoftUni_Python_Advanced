from collections import deque

people = deque()

while True:
    name = input()

    if name == "End":
        break
    elif name == "Paid":
        while people:
            print(people.popleft())
        continue

    people.append(name)

print(f"{len(people)} people remaining.")
