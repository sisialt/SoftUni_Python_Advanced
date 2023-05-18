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

# odd_set = set()
# even_set = set()
#
# for row in range(1, int(input()) + 1):
#     ascii_sum_of_name = sum(ord(l) for l in input()) // row
#
#     # even_set.add(ascii_sum_of_name) if ascii_sum_of_name % 2 == 0 else odd_set.add(ascii_sum_of_name)
#
#     if ascii_sum_of_name % 2 == 0:
#         even_set.add(ascii_sum_of_name)
#     else:
#         odd_set.add(ascii_sum_of_name)
#
# if sum(odd_set) > sum(even_set):
#     print(*odd_set.difference(even_set), sep=", ")
# else:
#     print(*odd_set.symmetric_difference(even_set), sep=", ")
