unique_names = set()

for _ in range(int(input())):
    name = input()
    unique_names.add(name)

print(*unique_names, sep='\n')
    