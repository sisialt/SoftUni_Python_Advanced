from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    nums_taken_count = 0

    while nums:
        current_num = nums.popleft()
        nums_taken_count += 1

        if nums_taken_count % 4 == 0:
            nums_taken_count = 0
            kwargs["m"] = kwargs["m"] * current_num

        elif nums_taken_count % 3 == 0:

            if current_num == 0:
                continue

            kwargs["d"] = kwargs["d"] / current_num

        elif nums_taken_count % 2 == 0:
            kwargs["s"] = kwargs["s"] - current_num

        else:
            kwargs["a"] = kwargs["a"] + current_num

    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted_dict])


# def math_operations(*numbers, **kwargs):
#     for i in range(len(numbers)):
#         key = list(kwargs.keys())[i % 4]
#
#         if key == "a":
#             kwargs[key] += numbers[i]
#         elif key == "s":
#             kwargs[key] -= numbers[i]
#         elif key == "d":
#             if numbers[i] != 0:
#                 kwargs[key] /= numbers[i]
#         elif key == "m":
#             kwargs[key] *= numbers[i]
#
#     kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#
#     return '\n'.join([f"{key}: {value:.1f}" for key, value in kwargs])



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
