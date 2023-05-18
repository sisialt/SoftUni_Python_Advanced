from collections import deque

boxes = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

presents = {}

while boxes and magic_levels:
    current_box = boxes.pop()
    current_magic_level = magic_levels.popleft()

    if not current_box and not current_magic_level:
        continue
    elif not current_box:
        magic_levels.appendleft(current_magic_level)
        continue
    elif not current_magic_level:
        boxes.append(current_box)
        continue

    total_magic = current_box * current_magic_level

    if total_magic == 150:

        if "Doll" not in presents:
            presents["Doll"] = 0
        presents["Doll"] += 1

    elif total_magic == 250:

        if "Wooden train" not in presents:
            presents["Wooden train"] = 0
        presents["Wooden train"] += 1

    elif total_magic == 300:

        if "Teddy bear" not in presents:
            presents["Teddy bear"] = 0
        presents["Teddy bear"] += 1

    elif total_magic == 400:

        if "Bicycle" not in presents:
            presents["Bicycle"] = 0
        presents["Bicycle"] += 1

    else:
        if total_magic < 0:
            total_magic = current_magic_level + current_box
            boxes.append(total_magic)
        elif total_magic > 0:
            boxes.append(current_box + 15)

if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes or magic_levels:
    if boxes:
        boxes.reverse()
        print(f"Materials left: {', '.join([str(x) for x in boxes])}")

    if magic_levels:
        print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for present, count in sorted(presents.items()):
    print(f"{present}: {count}")

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0