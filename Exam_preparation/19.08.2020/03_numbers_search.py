def numbers_searching(*args):
    given_numbers = [arg for arg in args]
    searched_numbers = []
    missing_num = 0

    max_num = max(given_numbers)
    min_num = min(given_numbers)

    for n in range(min_num, max_num + 1):
        if n not in given_numbers:
            missing_num = n
        else:
            if given_numbers.count(n) > 1:
                searched_numbers.append(n)

    return [missing_num, searched_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print()
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print()
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))