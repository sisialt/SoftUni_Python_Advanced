longest_intersection = set()

for _ in range(int(input())):
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")

    first_set = set()
    second_set = set()

    for i in range(int(first_range[0]), int(first_range[1]) + 1):
        first_set.add(i)

    for i in range(int(second_range[0]), int(second_range[1]) + 1):
        second_set.add(i)

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [el.split(",") for el in input().split("-")]  # ["3,4", "1,2"] => [[3, 4], [1, 2]]
#
#     first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
#     second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
#
#     intersection = first_range.intersection(second_range)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(
#     f"Longest intersection is "
#     f"[{', '.join(str(x) for x in longest_intersection)}] "
#     f"with length {len(longest_intersection)}"
# )
