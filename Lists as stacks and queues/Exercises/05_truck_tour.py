from collections import deque

number_petrol_pumps = int(input())
pumps = deque()

for pump in range(number_petrol_pumps):
    petrol, km_to_next_pump = [int(x) for x in input().split()]
    pumps.append([pump, petrol, km_to_next_pump])

while True:
    counter = 1
    distance_driven = 0
    truck_capacity = 0

    for pump in pumps:
        distance_to_next = pump[2]
        petrol_filled = pump[1]
        truck_capacity += petrol_filled

        if truck_capacity >= distance_to_next:
            counter += 1
            distance_driven += distance_to_next
            truck_capacity -= distance_to_next
        else:
            pumps.rotate(-counter)
            break
    else:
        break

print(pumps.popleft()[0])

# pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
#
# pumps_data_copy = pumps_data.copy()
# gas_in_tank = 0
# index = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#
#     gas_in_tank += petrol
#
#     if gas_in_tank >= distance:
#         gas_in_tank -= distance
#     else:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         index += 1
#         gas_in_tank = 0
#
# print(index)
