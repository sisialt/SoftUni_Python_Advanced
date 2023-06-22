from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

rotations = 0
taken_seats = []

while rotations != 10:
    current_first = first_sequence.popleft()
    current_second = second_sequence.pop()

    current_char = chr(current_first + current_second)
    rotations += 1

    for seat in seats:
        if str(current_first) + current_char == seat or str(current_second) + current_char == seat:
            if seat not in taken_seats:
                taken_seats.append(seat)
                break
    else:
        first_sequence.append(current_first)
        second_sequence.appendleft(current_second)

    if len(taken_seats) == 3:
        break

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")

# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46
#
# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40
#
# 15C, 25C, 36C, 43P, 40E, 38G
# 15, 25, 80, 40, 15, 99, 52
# 15, 42, 29
