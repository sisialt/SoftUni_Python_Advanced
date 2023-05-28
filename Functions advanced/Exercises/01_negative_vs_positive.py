def positive_or_negative(nums):
    for num in nums:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)


numbers = [int(x) for x in input().split()]

positive_numbers = []
negative_numbers = []

positive_or_negative(numbers)

positive_sum = sum(positive_numbers)
negative_sum = sum(negative_numbers)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
