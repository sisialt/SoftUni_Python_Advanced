def grocery_store(**kwargs):
    result = ""

    sort_by_quantity_and_len_name = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for key, value in sort_by_quantity_and_len_name:
        result += f"{key}: {value}" + "\n"

    return result


# def grocery_store(**products):
#     products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     return '\n'.join([f"{p}: {q}" for p, q in products])
#

# def grocery_store(**products):
#     products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     result = []
#
#     for product, quantity in products:
#         result.append(f"{product}: {quantity}")
#
#     return '\n'.join(result)

print(grocery_store(
    bread=5, pasta=12, eggs=12,
))

print(grocery_store(
    bread=2, pasta=2, eggs=20, carrot=1,
))
