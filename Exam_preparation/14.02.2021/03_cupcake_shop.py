def stock_availability(inventory_list, kind, *args):
    if kind == "delivery":
        inventory_list.extend([arg for arg in args])

    elif kind == "sell":

        for arg in args:

            if str(arg).isdigit():
                [inventory_list.pop(0) for _ in range(arg)]
                break

            else:
                for cupcake in args:
                    while cupcake in inventory_list:
                        inventory_list.remove(cupcake)

        if not args:
            inventory_list.pop(0)

    return inventory_list



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
