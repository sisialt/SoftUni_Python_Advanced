from collections import deque

food = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])
peaks = deque([
    ["Vihren", 80],
    ["Kutelo", 90],
    ["Banski Suhodol", 100],
    ["Polezhan", 60],
    ["Kamenitza", 70],
])

conquered_peaks = []

for i in range(1, 8):
    current_food = food.pop()
    current_stamina = stamina.popleft()
    current_peak = peaks.popleft()

    current_peak_name = current_peak[0]
    current_peak_difficulty_level = current_peak[1]

    sum_food_stamina = current_food + current_stamina

    if sum_food_stamina >= current_peak_difficulty_level:
        conquered_peaks.append(current_peak_name)
    else:
        peaks.appendleft(current_peak)

    if not peaks:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print(*conquered_peaks, sep="\n")


# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2
#
# 10, 20, 34, 26, 12, 10, 45
# 30, 28, 17, 17, 13, 10, 10
