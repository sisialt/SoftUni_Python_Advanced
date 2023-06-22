from collections import deque


def check_range():
    for gift, value in gifts.items():
        if sum_material_magic in range(value[0], value[1] + 1):
            if gift not in crafted_presents:
                crafted_presents[gift] = 0
            crafted_presents[gift] += 1
            break


materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": [100, 199],
    "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399],
    "Diamond Jewellery": [400, 499]
}

crafted_presents = {}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()

    sum_material_magic = current_material + current_magic_level

    check_range()

    if sum_material_magic < 100:
        if sum_material_magic % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            sum_material_magic = current_material + current_magic_level
        else:
            sum_material_magic *= 2

        check_range()

    elif sum_material_magic > 499:
        sum_material_magic //= 2  # it was /=
        check_range()

if ("Gemstone" in crafted_presents and "Porcelain Sculpture" in crafted_presents) or\
        ("Gold" in crafted_presents and "Diamond Jewellery" in crafted_presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for gift, count in crafted_presents.items():
    print(f"{gift}: {count}")


# 105 20 30 25
# 120 60 11 400 10 1
#
# 30 5 21 6 0 91
# 15 9 5 15 8
#
# 200
# 5 15 32 20 10 5
