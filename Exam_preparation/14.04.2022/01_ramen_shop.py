from collections import deque

bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while bowls and customers:
    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        current_bowl -= current_customer
        bowls.append(current_bowl)
    elif current_customer > current_bowl:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")


# 14, 25, 37, 43, 19
# 58, 23, 37
#
# 30, 13, 45
# 70, 25, 55, 15
#
# 30, 25
# 20, 35
