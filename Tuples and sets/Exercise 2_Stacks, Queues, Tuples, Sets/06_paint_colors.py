from collections import deque

substrings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

colors_found = []
secondary_colors_found = {}
count_colors_found = 0

while substrings:
    first_substring = substrings.popleft()
    last_substring = substrings.pop() if substrings else ""

    color = first_substring + last_substring
    color_second_combination = last_substring + first_substring

    if color in main_colors:
        count_colors_found += 1
        colors_found.append(color)
    elif color_second_combination in main_colors:
        count_colors_found += 1
        colors_found.append(color_second_combination)
    elif color in secondary_colors:
        count_colors_found += 1
        secondary_colors_found[color] = count_colors_found
    elif color_second_combination in secondary_colors:
        count_colors_found += 1
        secondary_colors_found[color_second_combination] = count_colors_found
    else:
        for el in (first_substring[:-1], last_substring[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

        # first_substring = deque([ch for ch in first_substring])
        #
        # first_substring.pop()
        #
        # last_substring = deque([ch for ch in last_substring])
        # last_substring.pop()
        #
        # for _ in range(len(substrings) // 2):
        #     removed_el = substrings.popleft()
        #     removed.append(removed_el)
        #
        # if last_substring:
        #     substrings.appendleft(''.join(list(last_substring)))
        #
        # if first_substring:
        #     substrings.appendleft(''.join(list(first_substring)))
        #
        # while removed:
        #     substrings.appendleft(removed.pop())

if secondary_colors_found:
    for col, index in secondary_colors_found.items():

        if col == "orange":
            if "red" in colors_found and "yellow" in colors_found:
                colors_found.insert(index - 1, col)
        elif col == "purple":
            if "red" in colors_found and "blue" in colors_found:
                colors_found.insert(index - 1, col)
        elif col == "green":
            if "blue" in colors_found and "yellow" in colors_found:
                colors_found.insert(index - 1, col)

print(colors_found)


# from collections import deque
#
# words = deque(input().split())  # d yel blu e low redd
#
# colors = {"red", "yellow", "blue", "orange", "purple", "green"}
# req_colors = {
#     "orange": {"yellow", "red"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"},
# }
#
# result = []
#
# while words:
#     first_word = words.popleft()
#     second_word = words.pop() if words else ''
#
#     for color in (first_word + second_word, second_word + first_word):
#         if color in colors:
#             result.append(color)
#             break
#     else:
#         for el in (first_word[:-1], second_word[:-1]):
#             if el:
#                 words.insert(len(words) // 2, el)
#
# for color in set(req_colors.keys()).intersection(result): # iterate over every secondary color that we have
#     if not req_colors[color].issubset(result):  # check if we have the needed colors to have the secondary color
#         result.remove(color)
#
# print(result)
