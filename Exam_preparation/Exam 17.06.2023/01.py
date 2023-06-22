from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while substances and tools:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)

        current_substance -= 1

        if current_substance != 0:
            substances.append(current_substance)

if challenges:
    print(f"Harry is lost in the temple. Oblivion awaits him.")
else:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")

# 2 4 6 8
# 11 3 5 7 9
# 24 28 18 30
#
# 13 7 4 22 11 15 20
# 3 2 1
# 12 10 5
