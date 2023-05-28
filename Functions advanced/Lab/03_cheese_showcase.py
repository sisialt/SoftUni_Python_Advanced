def sorting_cheeses(**kwargs):
    res = ""

    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for cheese in sorted_cheese:
        res += cheese[0] + '\n'
        res += '\n'.join([str(x) for x in sorted(cheese[1], reverse=True)]) + '\n'

    return res


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )

)