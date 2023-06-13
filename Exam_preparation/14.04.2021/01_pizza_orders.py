from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])

total_pizzas = 0

while pizza_orders and employees:
    current_pizzas = pizza_orders.popleft()

    if current_pizzas <= 0 or current_pizzas > 10:
        continue

    current_employee = employees.pop()

    if current_pizzas <= current_employee:
        total_pizzas += current_pizzas
    else:
        current_pizzas -= current_employee
        total_pizzas += current_employee
        pizza_orders.appendleft(current_pizzas)

if employees:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizzas}\n"
          f"Employees: {', '.join(str(x) for x in employees)}")

if pizza_orders:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
''
#
# 11, 6, 8, 1
# 3, 1, 9, 10, 5, 9, 1

# 10, 9, 8, 7, 5
# 5, 10, 9, 8, 7
#
# 12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1
