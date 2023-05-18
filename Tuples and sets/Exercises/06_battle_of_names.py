set_odd = set()
set_even = set()

for i in range(1, int(input()) + 1):
    name = input()
    sum_ascii = 0

    for ch in name:
        sum_ascii += ord(ch)

    result = sum_ascii // i

    set_odd.add(result) if result % 2 == 1 else set_even.add(result)

sum_set_odd = sum(set_odd)
sum_set_even = sum(set_even)

if sum_set_odd == sum_set_even:
    print(*set_odd.union(set_even), sep=', ')
elif sum_set_odd > sum_set_even:
    print(*set_odd.difference(set_even), sep=', ')
else:
    print(*set_odd.symmetric_difference(set_even), sep=', ')
