numbers = [int(x) for x in input().split(", ")]
numbers_as_dict = {}

for i, num in enumerate(numbers):
    if num not in numbers_as_dict:
        numbers_as_dict[num] = [i]
    else:
        numbers_as_dict[num].append(i)


numbers_copy = numbers.copy()
task_index = int(input())

jobs = 0

while True:
    min_num = float("inf")

    for num in numbers_copy:
        if num < min_num:
            min_num = num

    jobs += min_num
    numbers_copy.remove(min_num)

    if numbers_as_dict[min_num][0] == task_index:
        break

    if len(numbers_as_dict[min_num]) == 1:
        del numbers_as_dict[min_num]
    else:
        numbers_as_dict[min_num].pop(0)

print(jobs)


# 3, 1, 10, 1, 2
# 0
#
# 4, 10, 10, 6, 2, 99
# 2
