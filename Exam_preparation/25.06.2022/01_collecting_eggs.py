from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
pieces_paper = deque([int(x) for x in input().split(", ")])

BOX_SIZE = 50
count_filled_boxes = 0

while eggs and pieces_paper:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    elif current_egg == 13:
        first_piece = pieces_paper.popleft()
        last_piece = pieces_paper.pop()
        pieces_paper.appendleft(last_piece)
        pieces_paper.append(first_piece)
        continue

    current_piece_paper = pieces_paper.pop()

    if current_egg + current_piece_paper <= BOX_SIZE:
        count_filled_boxes += 1

if count_filled_boxes:
    print(f"Great! You filled {count_filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if pieces_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_paper])}")

# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9
#
# 2, 4, 7, 8, 0
# 5, 6, 2
#
# 12, 23
# 28, 40
