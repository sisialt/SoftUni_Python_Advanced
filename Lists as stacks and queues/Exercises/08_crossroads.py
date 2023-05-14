from collections import deque

green_light_duration = int(input())
free_window = int(input())

cars = deque()
counter_passed_cars = 0
car_crash = False

while not car_crash:
    car = input()

    if car == "END":
        break
    elif car != "green":
        cars.append(car)
    else:
        left_green_light = green_light_duration

        while left_green_light > 0 and cars:
            first_car = cars.popleft()

            time = left_green_light + free_window

            if len(first_car) > time:
                print(f"A crash happened!\n{first_car} was hit at {first_car[time]}.")
                car_crash = True

            left_green_light -= len(first_car)
            counter_passed_cars += 1

if not car_crash:
    print(f"Everyone is safe.\n{counter_passed_cars} total cars passed the crossroads.")
