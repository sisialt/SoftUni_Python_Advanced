from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy_used, toys = 0, 0
count_taken_boxes = 0

while elves and materials:
    current_energy = elves.popleft()

    if current_energy < 5:
        continue

    count_taken_boxes += 1

    current_materials = materials.pop()

    if count_taken_boxes % 3 == 0:
        current_materials *= 2

    if current_energy >= current_materials:
        toys += 1
        current_energy -= current_materials
        current_energy += 1
        total_energy_used += current_materials

        if count_taken_boxes % 3 == 0:
            toys += 1

        if count_taken_boxes % 5 == 0:
            toys -= 1
            current_energy -= 1

        if count_taken_boxes % 15 == 0:
            toys -= 1

    else:
        if count_taken_boxes % 3 == 0:
            current_materials //= 2

        materials.append(current_materials)
        current_energy *= 2

    if current_energy:
        elves.append(current_energy)

print(f"Toys: {toys}")
print(f"Energy: {total_energy_used}")

if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")

if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")

    # logic 32-37 lines (%15/%5)
    # line 46 not necessary

    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

# from collections import deque
#
# elves = deque([int(x) for x in input().split()])
# materials = deque([int(x) for x in input().split()])
#
# total_energy = 0
# total_toys = 0
# iterations = 0
#
# while elves and materials:
#     elf = elves.popleft()
#     material = materials[-1]
#
#     if elf < 5:
#         continue
#
#     iterations += 1
#     current_toys_count = 0
#
#     if iterations % 3 == 0:
#         material *= 2
#         current_toys_count += 1
#
#     if elf >= material:
#         total_energy += material
#         elf -= material
#
#         if iterations % 5 != 0:
#             elf += 1
#             current_toys_count += 1
#         else:
#             current_toys_count = 0
#
#         materials.pop()
#     else:
#         elf *= 2
#         current_toys_count = 0
#
#     total_toys += current_toys_count
#
#     elves.append(elf)
#
# print(f"Toys: {total_toys}")
# print(f"Energy: {total_energy}")
#
# if elves:
#     print(f"Elves left: {', '.join(str(x) for x in elves)}")
#
# if materials:
#     print(f"Boxes left: {', '.join(str(x) for x in materials)}")
