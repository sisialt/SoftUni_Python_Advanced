from collections import deque
import time

unique_integers = deque([int(x) for x in input().split()])
target = int(input())

start_with_two_loops = time.time()

while unique_integers:
    num1 = unique_integers.popleft()
    for num2 in unique_integers:
        if num2 + num1 == target:
            unique_integers.remove(num2)
            print(f"{num1} + {num2} = {target}")
            break

end_time_two = time.time()
print(f"Two loops time: {end_time_two - start_with_two_loops}")

unique_integers = deque([int(x) for x in input().split()])
target = int(input())

targets = set()
values_map = {}

start_one_loop = time.time()

for value in unique_integers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value

end_time_one = time.time()
print(f"One loop time: {end_time_one - start_one_loop}")
