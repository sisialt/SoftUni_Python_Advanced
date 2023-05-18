text = tuple(input())

unique_symbols = set()

for ch in text:
    unique_symbols.add(ch)

for ch in sorted(unique_symbols):
    print(f"{ch}: {text.count(ch)} time/s")

# occurrences = {}
# for ch in text:
#     if ch not in occurrences:
#         occurrences[ch] = 0
#     occurrences[ch] += 1
#
# for ch, occ in sorted(occurrences.items()):
#     print(f"{ch}: {occ} time/s")
