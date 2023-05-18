text = tuple(input())

unique_symbols = set(text)

for ch in sorted(unique_symbols):
    print(f"{ch}: {text.count(ch)} time/s")

# occurrences = {}
# for ch in input():
#     if ch not in occurrences:    occurrences[ch] = occurrences.get(ch, 0) + 1
#         occurrences[ch] = 0
#     occurrences[ch] += 1
#
# for ch, occ in sorted(occurrences.items()):
#     print(f"{ch}: {occ} time/s")

# from collections import defaultdict
# occurrences = defaultdict(lambda: 0)
# for ch in input():
#     occurrences[ch] += 1
