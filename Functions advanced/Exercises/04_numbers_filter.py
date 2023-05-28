def even_odd_filter(**kwargs):
    for key in kwargs:
        if key == "odd":
            filtered_nums = [num for num in kwargs["odd"] if num % 2 != 0]
            kwargs["odd"] = filtered_nums
        else:
            filtered_nums = [num for num in kwargs["even"] if num % 2 == 0]
            kwargs["even"] = filtered_nums

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
odd=[2, 2, 30, 44, 10, 5],
))