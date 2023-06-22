def best_list_pureness(numbers, k):
    max_sum = 0
    best_rotation = 0

    for rotation in range(0, k + 1):
        sum_nums = 0
        for i, num in enumerate(numbers):
            sum_nums += num * i

        if sum_nums > max_sum:
            max_sum = sum_nums
            best_rotation = rotation

        numbers.insert(0, numbers.pop())

    return f"Best pureness {max_sum} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
#
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
