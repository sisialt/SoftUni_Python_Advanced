string = input().split("|")
substrings = [sub.split() for sub in string[::-1]]

[print(*inner, end=' ') for inner in substrings if inner]

# inner could be empty, forgot if inner

# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])


# line = input().split("|")  # прочитаме реда като го разделяме по черта
#
# sub_lists = []  # създаваме списък, в които ще пазим резултата
#
# for sub_string in line[::-1]:  # развъртаме цикъл, който обхожда всеки подтекст в инпута
#     sub_lists.extend(sub_string.split())
#     # удължаваме списъка с резултата със списък от числата от конзолата след като сме махнали всички спейсове
#
# print(*sub_lists)
