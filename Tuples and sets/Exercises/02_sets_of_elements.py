n, m = [int(x) for x in input().split()]

n_set, m_set = set(), set()

for i in range(n + m):
    number = int(input())
    if i < n:
        n_set.add(number)
    else:
        m_set.add(number)

unique_numbers_in_both_sets = n_set.intersection(m_set)
print(*unique_numbers_in_both_sets, sep='\n')
