n = int(input())

vip_guests = set()
guests = set()

for _ in range(n):
    guest = input()
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        guests.add(guest)

all_invited = vip_guests.union(guests)

while True:
    guest = input()

    if guest == "END":
        break

    if guest in all_invited:
        all_invited.remove(guest)

print(len(all_invited))
for g in sorted(all_invited):
    print(g)


