clothes = [int(x) for x in input().split()]
rank_capacity = int(input())

sum_clothes = 0
if not clothes:
    ranks_used = 0
else:
    ranks_used = 1

for _ in range(len(clothes)):
    current_piece_of_clothing = clothes.pop()
    if sum_clothes + current_piece_of_clothing > rank_capacity:
        sum_clothes = current_piece_of_clothing
        ranks_used += 1
    elif sum_clothes == rank_capacity:
        if clothes:
            sum_clothes = 0
            ranks_used += 1
    else:
        sum_clothes += current_piece_of_clothing

print(ranks_used)
