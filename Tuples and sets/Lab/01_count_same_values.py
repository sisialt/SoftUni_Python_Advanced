nums = tuple(float(x) for x in input().split())
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
        print(f"{num:.1f} - {nums.count(num)} times")
