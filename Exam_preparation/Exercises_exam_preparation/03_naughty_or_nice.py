def naughty_or_nice_list(names, *args, **kwargs):

    def find_only_one_count(value, given_command):
        count = 0

        for num, name in names:
            if num == value:
                count += 1

        if count == 1:
            for num, name in names:
                if num == value:
                    if given_command == "Nice":
                        nice.append(name)
                    else:
                        naughty.append(name)

                    names.remove((num, name))
                    break

    nice, naughty, not_found = [], [], []

    for arg in args:
        counting_number, nice_or_naughty = arg.split("-")

        find_only_one_count(int(counting_number), nice_or_naughty)

    for key, nice_or_naughty in kwargs.items():
        find_only_one_count(key, nice_or_naughty)

    for kid in names:
        not_found.append(kid[1])

    result = ""

    if nice:
        result += "Nice: "
        result += f"{', '.join(nice)}"
    if naughty:
        result += f"\nNaughty: "
        result += f"{', '.join(naughty)}"
    if not_found:
        result += f"\nNot found: "
        result += f"{', '.join(not_found)}"

    return result


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty", ))

print(naughty_or_nice_list( [ (7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ], "3-Nice", "5-Naughty", "2-Nice", "1-Nice", ))

print(naughty_or_nice_list( [ (6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ], "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty", ))


# def naughty_or_nice_list(santa_list, *args, **kwargs):
#     nice_kids, naughty_kids = [], []
#     result = []
#
#     def place_kid():
#         if len(kids) == 1:
#             nice_kids.append(kids[0][1]) if type_of_kid == "Nice" else naughty_kids.append(kids[0][1])
#             santa_list.remove(*kids)
#
#     for kid_data in args:
#         number, type_of_kid = kid_data.split("-")
#         kids = [info for info in santa_list if info[0] == int(number)]
#         place_kid()
#
#     for name, type_of_kid in kwargs.items():
#         kids = [info for info in santa_list if info[1] == name]
#         place_kid()
#
#     if nice_kids:
#         result.append(f"Nice: {', '.join(nice_kids)}")
#     if naughty_kids:
#         result.append(f"Naughty: {', '.join(naughty_kids)}")
#     if santa_list:
#         result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")
#
#     return "\n".join(result)