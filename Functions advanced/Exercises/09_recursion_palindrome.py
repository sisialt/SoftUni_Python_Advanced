def palindrome(word, index, reversed_word=""):
    if index != len(word):
        reversed_word += word[(len(word) - 1) - index]
        return palindrome(word, index + 1, reversed_word=reversed_word)

    if word == reversed_word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


# def palindrome(word, idx):
#     if idx == len(word) // 2:
#         return f"{word} is a palindrome"
#
#     if word[idx] != word[-idx-1]:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, idx + 1)

print(palindrome("abcba", 0))

print(palindrome("peter", 0))
