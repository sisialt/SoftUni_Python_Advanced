from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join(str(x) for x in customers)}")


# 4, 6, 8, 5, 1
# 1, 9, 15, 10, 6
#
# 10, 5, 8, 9
# 2, 4, 5, 8
#
# 2, 8, 4, 3, 11, 7
# 10, 15, 4, 6, 3, 10, 2, 1
