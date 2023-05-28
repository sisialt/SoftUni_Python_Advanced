def fill_the_box(h, l, w, *args):
    box_size = h * l * w
    cubes = 0

    for el in args:
        if not isinstance(el, int):
            break
        else:
            cubes += el

    if box_size > cubes:
        return f"There is free space in the box. You could put {box_size - cubes} more cubes."
    else:
        return f"No more free space! You have {cubes - box_size} more cubes."

# from collections import deque
#
#
# def fill_the_box(height, length, width, *cubes):
#     space = height * length * width
#     cubes = deque(cubes)
#
#     while cubes[0] != "Finish":
#         space -= cubes.popleft()
#
#         if space < 0:
#             cubes_left = sum(x for x in cubes if x != "Finish")
#             return f"No more free space! You have {cubes_left + abs(space)} more cubes."
#
#     return f"There is free space in the box. You could put {space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))