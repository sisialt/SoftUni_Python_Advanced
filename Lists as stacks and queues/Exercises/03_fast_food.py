from collections import deque

food_quantity = int(input())
orders = [int(x) for x in input().split()]
orders_as_deque = deque(orders)

print(max(orders))

for _ in range(len(orders_as_deque)):
    current_order = orders_as_deque.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders_as_deque.appendleft(current_order)
        print(f"Orders left: {' '.join(str(x) for x in list(orders_as_deque))}")
        break
else:
    print(f"Orders complete")


# food = int(input())
# orders = deque([int(x) for x in input().split()])
#
# print(max(orders))
#
# for order in orders.copy():
#     if food >= order:
#         orders.popleft()
#         food -= order
#     else:
#         print(f"Orders left: {' '.join([str(x) for x in orders])}")
#         break
# else:
#     print("Orders complete")
