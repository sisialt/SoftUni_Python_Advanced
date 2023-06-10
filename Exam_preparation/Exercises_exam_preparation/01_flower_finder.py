from collections import deque


def find_word(letter, ch_word, word):
    word_found = ""
    while True:
        if letter in ch_word:
            index = ch_word.index(letter)
            ch_word = ch_word[:index] + ch_word[index + 1:]

            if ch_word == "":
                ind = words_changed.index(word)
                word_found = words[ind]
                return word_found
        else:
            return word_found, ch_word


vowels = deque(input().split())
consonants = deque(input().split())

words = ["rose", "tulip", "lotus", "daffodil"]
words_changed = ["rose", "tulip", "lotus", "daffodil"]
result = ""
is_found = False

while vowels and consonants and not is_found:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words_changed:
        changed_word = word
        result = find_word(current_vowel, changed_word, word)

        if result[0]:
            is_found = True
            break

        result = find_word(current_consonant, result[1], word)

        if result[0]:
            is_found = True
            break

        words_changed[words_changed.index(word)] = result[1]

if result[0]:
    print(f"Word found: {result}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
#
# words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
#
# while vowels and consonants:
#     vowel = vowels.popleft()
#     consonant = consonants.pop()
#
#     for word in words:
#         words[word] = words[word].replace(vowel, '')
#         words[word] = words[word].replace(consonant, '')
#
#         if not words[word]:
#             print(f"Word found: {word}")
#             break
#     else:
#         continue
#
#     break
# else:
#     print("Cannot find any word!")
#
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
#
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")

# o e a o e a i
# p r s x r


