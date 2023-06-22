def shopping_list(budget, **kwargs):
    products = 0
    result = []

    if budget < 100:
        return "You do not have enough budget."

    for product, value in kwargs.items():
        total_price = value[0] * value[1]

        if total_price <= budget:
            budget -= total_price  # forgot
            products += 1

            result.append(f"You bought {product} for {total_price:.2f} leva.")

            if products == 5:
                break

    return '\n'.join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(
)

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
