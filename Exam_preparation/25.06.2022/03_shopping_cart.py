def shopping_cart(*args):
    cart = {"Soup": set(), "Pizza": set(), "Dessert": set()}  # it was empty
    result = []

    max_products = {"Soup": 3, "Pizza": 4, "Dessert": 2}

    for arg in args:
        if arg == "Stop":
            break

        meal = arg[0]
        product = arg[1]

        if len(cart[meal]) < max_products[meal]:
            cart[meal].add(product)

    cart = dict(sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])))

    for m in cart:
        if cart[m]:
            break
    else:
        return f"No products in the cart!"  # logic

    for meal in cart:
        result.append(f"{meal}:")
        prod = [f' - {product}' for product in sorted(cart[meal])]
        result.extend(prod)

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
