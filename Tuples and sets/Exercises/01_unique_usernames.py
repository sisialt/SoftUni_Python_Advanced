unique_usernames = set()

for _ in range(int(input())):
    name = input()
    unique_usernames.add(name)

print(*unique_usernames, sep='\n')

# print(*{input() for _ in range(int(input()))}, sep='\n')
