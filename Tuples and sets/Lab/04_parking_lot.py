parking = set()

for _ in range(int(input())):
    direction, car_number = input().split(', ')

    if direction == "IN":
        parking.add(car_number)
    elif direction == "OUT":
        parking.remove(car_number)

if not parking:
    print("Parking Lot is Empty")
else:
    for car in parking:
        print(car)

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA